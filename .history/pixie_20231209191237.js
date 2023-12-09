
function download(){
        var link = document.createElement('a');
        let l = document.getElementById("fileInput").value.replace(/^.*[\\/]/, '').split(".");
        link.download = l[0] + "-pixellated.png" ;
        link.href = document.getElementById('canvasOutputFull').toDataURL()
        link.click();
        
}
function pixellate(imgElement, pixelSize, colors){
    // source image
    // let imgElement = document.getElementById("imageSrc")
    let src = cv.imread(imgElement);
    //let pixelSize = Number(document.getElementById("pixelSize").value);
    let newWidth =  Math.floor(src.cols / pixelSize);
    let newHeight = Math.floor(src.rows / pixelSize);
    let dsize = new cv.Size(newWidth, newHeight);
    
    // resize smaller
    let dst = new cv.Mat(dsize, cv.CV_8SC4)
    cv.resize(src, dst, dsize, 0, 0, cv.INTER_AREA);
    src.delete();
    // copy back to src
    
    
    // apply convolution
    src = dst;
    // create new dst
    dst = new cv.Mat(dsize, cv.CV_8SC4)
    let kernel =   [-1, -1, -1, 
                    -1, 9, -1,
                    -1, -1, -1 ]
    let mat = cv.matFromArray(3, 3, cv.CV_8S, kernel)
    let anchor = new cv.Point(-1, -1);
    cv.filter2D(src, dst, -1, mat, anchor,0, cv.BORDER_DEFAULT);
    src.delete();
    
    // conver to RGB 
    src = dst;
    dst = new cv.Mat(dsize, cv.CV_8SC3)
    cv.cvtColor(src, dst, cv.COLOR_RGBA2RGB);
    src.delete();

        //recolour
        if (colors !== undefined && colors.length > 0){
        src = dst;
        //dst = new cv.Mat(dsize, cv.CV_8SC3)
        dst = src.clone();
        //let colors = [[255,0,0],[0,255,0],[0,0,255],[255,255,0],[255,0,255],[0,255,255],[255,255,255],[0,0,0]];
        //let colors = paletteGenerator(16,4,3);

        recolour(src, dst, colors);
        
        src.delete();
        }
    

    // copy back to src
    src = dst;
    // // create new dst
    dst = new cv.Mat(dsize, cv.CV_8SC4)
    // move back to RGBA
    cv.cvtColor(src, dst, cv.COLOR_RGB2RGBA);
    src.delete();

    // rescale up
    // copy back to src
    src = dst;
    // create new dst for upscaling
    let upWidth =  Math.floor(src.cols * pixelSize);
    let upHeight = Math.floor(src.rows * pixelSize);
    let updsize = new cv.Size(upWidth, upHeight);
    dst = new cv.Mat(updsize, cv.CV_8SC4)
    cv.resize(src, dst, updsize, 0, 0, cv.INTER_NEAREST);
    src.delete(); 

    // show image
    cv.imshow('canvasOutput', dst);
    cv.imshow('canvasOutputFull', dst);
    canvas = document.getElementById('canvasOutput');
    canvas.hidden = false;
    dst.delete();
    // show download button
    let butn = document.getElementById("download");
    butn.hidden = false;
    // move to image
    // 
    canvas.scrollIntoView({ behavior: "smooth", block: "start", inline: "nearest" });
};

function colorSim(color, color2){
    let sim = 0;
    for(let i = 0; i < color.length; i++){
        sim += Math.pow(color[i] - color2[i],2);
    }
    return Math.sqrt(sim);
}
function bestColor(color, colors){
    let best = colors[0]
    let bestSim = colorSim(color, colors[0]);
    for(let k = 1; k < colors.length; k++){
        let sim = colorSim(color, colors[k]);
        if(sim < bestSim){
            best = colors[k];
            bestSim = sim;
        }
    }
    return best;
}
function recolour(src, dst, colors){
    for (let i = 0; i < src.rows; i++) {
        for (let j = 0; j < src.cols; j++) {
            let pixel = src.ucharPtr(i, j);
            let best = bestColor(pixel, colors);
            dst.data.set(best, i * src.cols * src.channels() + j * src.channels());
            
        }
    }

}
function paletteGenerator(numberHues,numberSaturation,numberValues){
    let colours = [];
    for(let i = 0; i < numberHues; i++){
        for(let k=numberSaturation; k >= 0; k--){
            for(let j = numberValues; j >= 0; j--){
                let hue = i * (1 / numberHues);
                let saturation = k * (1 / numberSaturation);
                let value = j * (1/ numberValues);
                let color = hsl2rgb(hue,saturation,value);
                colours.push(color);
            }
        }
    }
    // remove duplicates
    let obj = {arr: colours};
    colours = uniqueArray(obj);
    return colours;
};
function hsv2rgb(h, s, v) {
    var r, g, b, i, f, p, q, t;
    i = Math.floor(h * 6);
    f = h * 6 - i;
    p = v * (1 - s);
    q = v * (1 - f * s);
    t = v * (1 - (1 - f) * s);
    switch (i % 6) {
        case 0: r = v, g = t, b = p; break;
        case 1: r = q, g = v, b = p; break;
        case 2: r = p, g = v, b = t; break;
        case 3: r = p, g = q, b = v; break;
        case 4: r = t, g = p, b = v; break;
        case 5: r = v, g = p, b = q; break;
    }
    return [ 
        Math.round(r * 255),
        Math.round(g * 255),
        Math.round(b * 255)];
    
}
function hue2rgb(p, q, t) {
    if (t < 0) t += 1;
    if (t > 1) t -= 1;
    if (t < 1/6) return p + (q - p) * 6 * t;
    if (t < 1/2) return q;
    if (t < 2/3) return p + (q - p) * (2/3 - t) * 6;
    return p;
    }
function hsl2rgb(h, s, l) {
    let r, g, b;
    
    if (s === 0) {
        r = g = b = l; // achromatic
    } else {
        const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        const p = 2 * l - q;
        r = hue2rgb(p, q, h + 1/3);
        g = hue2rgb(p, q, h);
        b = hue2rgb(p, q, h - 1/3);
    }
    
    return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
    }
function uniqueArray(obj) {
    const uniqueArray = obj.arr.filter((value, index) => {
        const _value = JSON.stringify(value);
        return index === obj.arr.findIndex(obj => {
        return JSON.stringify(obj) === _value;
        });
    });
    return uniqueArray;
    }
function component2hex(c) {
    var hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
    }
    
function rgb2hex(r, g, b) {
    return "#" + component2hex(r) + component2hex(g) + component2hex(b);
    }
function displayPalette(colors){
    let palette = document.getElementById("palette");
    // remove old palette
    while (palette.firstChild) {
        palette.removeChild(palette.firstChild);
    }
    for(let i = 0; i < colors.length; i++){
        let color = colors[i];
        let hex = rgb2hex(color[0],color[1],color[2]);
        let div = document.createElement("div");
        // add class
        div.classList.add("rounded");
        div.classList.add("m-1");
        div.style.backgroundColor = hex;
        div.style.width = "50px";
        div.style.height = "50px";
        div.style.display = "inline-block";
        palette.appendChild(div);
    }
}
function splitPaletteArgs(args){
    return args.split("-");
};
function generateGraScalePalette(n){
    let colors = [];

    for (let i = 0; i < n; i++){
        let fraction = i / n;
        let color = [fraction*256,fraction*256,fraction*256];
        colors.push(color);
    }
    return colors;
};
function removePalette(){
    let palette = document.getElementById("palette");
    // remove old palette
    while (palette.firstChild) {
        palette.removeChild(palette.firstChild);
    }
};
function customPalette(){
    let palette = JSON.parse(document.getElementById("paletteValues").value);
    
    document.getElementById("paletteValues").value = JSON.stringify(colors);
};
function changePalette(){

    // get palette
    let palette = document.getElementById("paletteChoice").value;
    // if palette is None, no palette
    if(palette === "None"){
        document.getElementById("paletteValues").value = "[]";
        removePalette();
        // hide palette by removing background class    
        document.getElementById("palette").hidden = true;
    }else{
        // unhide palette
        document.getElementById("palette").hidden = false;
        // get palette args
        console.log(palette);
        // if bk generate palette differently
        let colors = [];
        switch(palette){
            case "Minecraft":
                colors = [[255,255,255],[216,127,51],[178,76,216],[102,153,216],[229,229,51],[127,204,25],[242,127,165],[76,76,76],[153,153,153],[76,127,153],[127,63,178],[51,76,178],[102,76,51],[102,127,51],[153,51,51],[25,25,25]];
                break;
            case "NES":
                colors = [
                [124,124,124],
                [0,0,252],
                [0,0,188],
                [68,40,188],
                [148,0,132],
                [168,0,32],
                [168,16,0],
                [136,20,0],
                [80,48,0],
                [0,120,0],
                [0,104,0],
                [0,88,0],
                [0,64,88],
                [0,0,0],
                [0,0,0],
                [0,0,0],
                [188,188,188],
                [0,120,248],
                [0,88,248],
                [104,68,252],
                [216,0,204],
                [228,0,88],
                [248,56,0],
                [228,92,16],
                [172,124,0],
                [0,184,0],
                [0,168,0],
                [0,168,68],
                [0,136,136],
                [0,0,0],
                [0,0,0],
                [0,0,0],
                [248,248,248],
                [60,188,252],
                [104,136,252],
                [152,120,248],
                [248,120,248],
                [248,88,152],
                [248,120,88],
                [252,160,68],
                [248,184,0],
                [184,248,24],
                [88,216,84],
                [88,248,152],
                [0,232,216],
                [120,120,120],
                [0,0,0],
                [0,0,0],
                [252,252,252],
                [164,228,252],
                [184,184,248],
                [216,184,248],
                [248,184,248],
                [248,164,192],
                [240,208,176],
                [252,224,168],
                [248,216,120],
                [216,248,120],
                [184,248,184],
                [184,248,216],
                [0,252,252],
                [248,216,248],
                [0,0,0],
                [0,0,0],
                ];
                break;
            case "Grayscale":
                colors = generateGraScalePalette(16);
                break;
            case "Default":
                colors = paletteGenerator(8,4,3);
                break;
            case "Colorful":
                colors = paletteGenerator(32,4,3);
                break;
            case "Ultra Colorful":
                colors = paletteGenerator(32,6,5);
                break;
            case "Automatic":
                // wait 1 second for image to load
                setTimeout(function(){ 
                    colors = getPaletteFromImage(document.getElementById("imageSrc"));
                    displayPalette(colors);
                    // set palette values
                    document.getElementById("paletteValues").value = JSON.stringify(colors);
                }, 1);
                colors = getPaletteFromImage(document.getElementById("imageSrc"));
                break;
        }
        // display palette
        displayPalette(colors);
        // set palette values
        document.getElementById("paletteValues").value = JSON.stringify(colors);
    }
};
function getPaletteFromImage(img){
    let mat = cv.imread(img);
    // resize down to pixel size
    let pixelSize = Number(document.getElementById("pixelSize").value);
    let newWidth =  Math.floor(mat.cols / pixelSize);
    let newHeight = Math.floor(mat.rows / pixelSize);
    let dsize = new cv.Size(newWidth, newHeight);
    // resize smaller
    let dst = new cv.Mat(dsize, cv.CV_8SC4)
    cv.resize(mat, dst, dsize, 0, 0, cv.INTER_AREA);
    mat.delete();
    
    let rgbarray = buildRgb(dst.data);
    let palette = quantization(rgbarray, 1);
    let rgb = [];
    for (const element of palette){
        rgb.push([element.r, element.g, element.b]);
    }
    return rgb;
}
function getExtension(filename) {
    var parts = filename.split('.');
    return parts[parts.length - 1];
}
    
function isImage(filename) {
    var ext = getExtension(filename);
    switch (ext.toLowerCase()) {
        case 'jpg':
        case 'gif':
        case 'bmp':
        case 'png':
        case 'webp':
        case 'jpeg':
        //etc
        return true;
    }
    return false;
}
function imgValidation(){
    let input = document.getElementById("fileInput");
    let butn = document.getElementById("pixellate");
    if (!isImage(input.value)){
        // disable button
        butn.disabled = true;
        //
        input.classList.add( "is-invalid");
        const toastMessage = document.getElementById('toastMessage')
        toastMessage.innerHTML = "Error: file is not an image. Supported formats: jpg, jpeg, gif, bmp, png, webp"
        const toastLiveExample = document.getElementById('liveToast')
        const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
        toastBootstrap.show()
        return false;
    }
    else{
        input.classList.remove( "is-invalid");
        return true;
    }
}
function pixelSizeValidation(){
    let input = document.getElementById("pixelSize");
    let min = 1;
    //let max = 1000;
    // check if value is a number
    let value = Number(input.value);
    if (isNaN(value) || value < min ){
        // disable button
        let butn = document.getElementById("pixellate");
        butn.disabled = true;
        input.classList.add( "is-invalid");
        const toastMessage = document.getElementById('toastMessage')
        toastMessage.innerHTML = "Error: Pixel size must be a number between " + min + " and " + max + "."
        const toastLiveExample = document.getElementById('liveToast')
        const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
        toastBootstrap.show()
        return false;
    }else{
        input.classList.remove( "is-invalid");
        return true;
    }
}
function pixelOverSizeValidation(){
    let input = document.getElementById("pixelSize");
    // wait 1 ms before taking image size
    let img = document.getElementById("imageSrc");
    console.log(img);
    let size = Number(input.value);
    if (size > img.width || size > img.height){
        // disable button
        let butn = document.getElementById("pixellate");
        butn.disabled = true;
        input.classList.add( "is-invalid");
        const toastMessage = document.getElementById('toastMessage')
        toastMessage.innerHTML = "Error: Pixel size "+ size+" must be smaller than both dimensions of image size " + img.width  + "x" + img.height + "."
        const toastLiveExample = document.getElementById('liveToast')
        const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
        toastBootstrap.show()
        return false;
    }
else{
    input.classList.remove( "is-invalid");
    return true;
}
}
function timeOutValidation(){
    setTimeout(inputValidation, 1);
}
function inputValidation(){
    // wait 1 ms
    let img = imgValidation();
    let pixel = pixelSizeValidation();
    // rechange the palette if needed
    let pixelOver = pixelOverSizeValidation();
    let butn = document.getElementById("pixellate");
    if(img && pixel && pixelOver){
        changePalette();
        // check that pixel size is not larger than either image width or height
        butn.disabled = false;
    }
    else{
        butn.disabled = true;
    }
}

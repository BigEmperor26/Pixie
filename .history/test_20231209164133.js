let example = [[200,0,0], [0,200,0], [0,0,200]];
// add element to the page
let img = document.createElement('img');
img.src = 'assets/img.png';
document.body.appendChild(img);
// create a canvas
let canvas = document.createElement('canvas');
canvas.width = img.width;
canvas.height = img.height;
document.body.appendChild(canvas);

// call pixellate

pixellate(img, canvas, example);
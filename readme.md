# PIXIE
## Javascript PixelArt generator
### Powered by OpenCV JS

This is a repository containg a simple code to automatically generate nice looking pixelart.

It provides the features of automatic pixellation with edge enhance to outline the edges of the images nicely. It also supports recolouring of the image with color palettes.

#### Live Demo

[<img src="assets/vercel.png" width=100>](https://pixie-alpha.vercel.app/) 

https://pixie-alpha.vercel.app/
#### Examples

|![alt text](assets/img.png "Title")|![alt text](assets/pixellated/luffy-5px.png "Title")|
|---|---|
|![alt text](assets/kanegawa.jpg "Title")|![alt text](assets/pixellated/kanegawa.png "Title")|
|![alt text](assets/sanji.webp "Title")|![alt text](assets/pixellated/sanji-5px.png "Title")|
|![alt text](assets/obama.jpeg "Title")|![alt text](assets/pixellated/Obama%20pix.png "Title")|

#### FAQ

##### Why? Isn't just a resize of the image ?
No, because there is also a sharpening phase involved, otherwise the result would just look blurry instead

See this example
|Original|Simple Resize|Pixie without recoloring| Pixie|
|---|---|---|---|
|![alt text](assets/img.png "Title")|![alt text](assets/luffy-blurry.png "Title")|![alt text](assets/pixellated/luffy-pixellated.png "Title")|![alt text](assets/pixellated/img-pixellated-auto-colour.png "Title")|

##### Is my data safe ? 
Yes, your pictures never leave your device. Network is only required to load the page.

#### Files

|file|description|
|---|---|
|`pixie.js`| file with the pixellation code|
|`opencv.js` | opencv dependency|

#### API

```js
// requires opencv.js 
function pixellate(imgElement, pixelSize, colors)
- imgElement: HTML image element of the page
- pixelSize: number of pixels of the original image to merge. Can be a float or int, from 0 to min(img.width, img.height)
- colors: list of colors in this RGB format
    if list is empty or undefined, no recoloring will be done. Otherwise recolouring using
```

#### API example
```js
let example_palette = [[200,0,0], [0,200,0], [0,0,200]];
// add element to the page
let img = document.getElementById('img');

// create a canvas openCV object
let canvas = document.getElementById('canvas');

// call pixellate
// 10 is the pixel size
pixellate(img, canvas, 10, example_palette);
```

#### Credits

- Automatic color palette extraction done using this repo
https://github.com/zygisS22/color-palette-extraction.git 

- OpenCV for the js enviroment
- Bootstrap for the UI
- Vercel for hosting
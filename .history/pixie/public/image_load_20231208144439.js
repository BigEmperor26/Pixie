let imgElement = document.getElementById("imageSrc")
let inputElement = document.getElementById("fileInput");
inputElement.addEventListener("click", (e) => {
    console.log("clocked");
imgElement.src = URL.createObjectURL(e.target.files[0]);
}, false);
console.log("image_load.js loaded");
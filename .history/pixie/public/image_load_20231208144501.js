let imgElement = document.getElementById("imageSrc")
let inputElement = document.getElementById("fileInput");
inputElement.addEventListener("click", (e) => {
    console.log("clocked");
imgElement.src = URL.createObjectURL(/sanji.webp);
}, false);
console.log("image_load.js loaded");
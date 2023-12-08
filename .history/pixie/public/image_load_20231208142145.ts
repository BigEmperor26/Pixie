let imgElement = document.getElementById("imageSrc")
if (!imgElement) {
    throw new Error("imgElement not found");
}
let inputElement = document.getElementById("fileInput");
if (!inputElement) {
    throw new Error("inputElement not found");
}

inputElement.addEventListener("change", (e) => {

    imgElement.src = URL.createObjectURL(e.target.files[0]);
}, false);

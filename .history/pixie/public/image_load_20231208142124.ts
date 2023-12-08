let imgElement = document.getElementById("imageSrc")
let inputElement = document.getElementById("fileInput");
if (!inputElement) {
    throw new Error("inputElement not found");
}
else {if(!imgElement) {
    throw new Error("imgElement not found");
}else{
    inputElement.addEventListener("change", (e) => {

        imgElement.src = URL.createObjectURL(e.target.files[0]);
    }, false);
}}
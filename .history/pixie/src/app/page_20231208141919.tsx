import React from 'react'
import Script from 'next/script'

const ImageComponent = () => {
  const imageUrl = 'https://example.com/image.jpg'; // Replace with your image URL

  return (
    <div>
    <div class="inputoutput">
      <img id="imageSrc" alt="No Image" />
      <div class="caption">imageSrc <input type="file" id="fileInput" name="file" /></div>
    </div>
  </div>
  <Script >
  let imgElement = document.getElementById("imageSrc")
  let inputElement = document.getElementById("fileInput");
  inputElement.addEventListener("change", (e) => {
    imgElement.src = URL.createObjectURL(e.target.files[0]);
  }, false);
  </Script>
  );
};

export default ImageComponent;
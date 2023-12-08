import React from 'react';

const ImageComponent = () => {
  const imageUrl = 'https://example.com/image.jpg'; // Replace with your image URL

  return (
    <div>
      <h1>Your Image</h1>
      <img src={imageUrl} alt="Description of your image" />
    </div>
  );
};

export default ImageComponent;
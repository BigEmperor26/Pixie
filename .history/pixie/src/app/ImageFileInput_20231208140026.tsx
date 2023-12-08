from React, { useState } from "react";
// components/ImageFileInput.tsx
type Props = {
    onFilesChange(files: File[]): void;
  };
  
  const ImageFileInput = ({ onFilesChange }: Props) => {
    return (
      <input
        type="file"
        accept="image/*" // only accept image file types
        multiple // allow multiple images
        onChange={(e) => {
          // this gives us the data on what files are selected
          // however, it's of type `FileList` which is hard to modify.
          const fileList = e.target.files;
          // let's convert `FileList` into a `File[]`
          if (fileList) {
            const files = [...fileList]; // now we have `File[]` type
            // This only works on es6 version make sure to set your tsconfig.json "target" to "es6"
            onFilesChange(files);
          }
        }}
        className="bg-gray-100"
      />
    );
  };
  export default ImageFileInput;
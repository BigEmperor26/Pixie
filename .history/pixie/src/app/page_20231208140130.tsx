'use client'
import ImageFileInput from "./components/ImageFileInput";
import { useState } from "react";

export default function Home() {
  // track the files selected using a useState hook.
  const [files, setFiles] = useState<File[]>([]);

  return (
    <main className="p-24">
      <ImageFileInput
        onFilesChange={(selectedFilies) => setFiles(selectedFilies)}
      />
      {/* iterate through the files and display the name */}
      {files.map((file, i) => {
        return <p key={i}>{file.name}</p>;
      })}
    </main>
  );
}

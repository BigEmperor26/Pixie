import * as React from 'react';
import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
 

export default function Page() {
  return (
    <Button component="label" variant="contained" startIcon={<CloudUploadIcon />}>
    Upload file
    <VisuallyHiddenInput type="file" />
  </Button>
    <img src="/sanji.webp" alt="pixie" width="300"/>
  );
}
import * as React from 'react';
import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import Container from '@mui/material/Container';
import Stack from '@mui/material/Stack';
import Script from 'next/script';


export default function Page() {
  return (
    <Container>
      <Script src="/image_load.js" />
      <Stack spacing={2} >
    <Button id="fileInput" component="label" variant="contained" startIcon={<CloudUploadIcon />}>
    Upload file
    {/* <VisuallyHiddenInput type="file" /> */}
    </Button>

    <img src="/sanji.webp" alt="pixie" width="300" id="imgSrc"/>
    </Stack>
    </Container>
  );
}
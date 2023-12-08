'use client'
import * as React from 'react';

import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import Container from '@mui/material/Container';
import Stack from '@mui/material/Stack';
import Script from 'next/script';

const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
});

export default function Page() {

  return (
    <Container>
      <Script src="/image_load.js" />
      <Stack spacing={2} >
    <Button id="fileInput" component="label" variant="contained" startIcon={<CloudUploadIcon />}>
    Upload file
    <VisuallyHiddenInput type="file" />
    </Button>

    <img src="/sanji.webp" alt="pixie" width="300" id="imgSrc"/>
    </Stack>
    </Container>
  );
}
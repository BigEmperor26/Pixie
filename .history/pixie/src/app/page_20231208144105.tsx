import * as React from 'react';
import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import Container from '@mui/material/Container';
import Stack from '@mui/material/Stack';


export default function Page() {
  return (
    <Container>
      <Stack spacing={2} >
    <Button component="label" variant="contained" startIcon={<CloudUploadIcon />}>
    Upload file
    {/* <VisuallyHiddenInput type="file" /> */}
    </Button>

    <img src="/sanji.webp" alt="pixie" width="300" id="imgSrc"/>
    </Stack>
    </Container>
  );
}
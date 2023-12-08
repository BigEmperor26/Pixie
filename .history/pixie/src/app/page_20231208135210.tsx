import * as React from 'react';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import * as React from 'react';
import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

export default function BasicButtonGroup() {
  return (
    <Button component="label" variant="contained" startIcon={<CloudUploadIcon />}>
  Upload file
  <VisuallyHiddenInput type="file" />
</Button>
  );
}

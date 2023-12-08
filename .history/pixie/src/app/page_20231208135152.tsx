import * as React from 'react';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import VisuallyHiddenInput from '@mui/material/VisuallyHiddenInput';

export default function BasicButtonGroup() {
  return (
    <Button component="label" variant="contained" startIcon={<CloudUploadIcon />}>
  Upload file
  <VisuallyHiddenInput type="file" />
</Button>
  );
}

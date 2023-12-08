import { *} from '@mui/material';

export default  function Page() {
  return (
  <Button component="label" variant="contained" startIcon={<CloudUploadIcon />}>
    Upload file
    <VisuallyHiddenInput type="file" />
  </Button>
    );
}
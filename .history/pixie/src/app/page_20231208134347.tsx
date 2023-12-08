import { Button} from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

export default  function Page() {
  return (
  <Button component="label" variant="contained" startIcon={<CloudUploadIcon />}>
    Upload file
    <VisuallyHiddenInput type="file" />
  </Button>
    );
}
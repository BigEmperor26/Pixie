import * as React from 'react';
import Button from '@mui/material/Button';
import { ButtonGroup } from '@mui/material/ButtonGroup';

export default function ButtonUsage() {
  // return <Button variant="contained">Hello world</Button>;
  return 
  <ButtonGroup variant="contained" aria-label="outlined primary button group">
  <Button>One</Button>
  <Button>Two</Button>
  <Button>Three</Button>
</ButtonGroup> ;
}
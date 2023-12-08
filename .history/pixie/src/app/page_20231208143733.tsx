import Image from 'next/image'
import { Button } from 'react-bootstrap';
 

export default function Page() {
  return (
    <Button variant="primary">Primary</Button>
    <img src="/sanji.webp" alt="pixie" width="300"/>
  );
}
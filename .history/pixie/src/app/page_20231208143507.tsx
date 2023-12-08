import Image from 'next/image'
 
export default function Page() {
  return (
    <Image
      src="/sanji.webp"
      width={500}
      height={500}
      alt="Picture of the author"
    />
  );
}
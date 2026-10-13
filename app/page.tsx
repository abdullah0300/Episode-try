import PageView from "@/components/PageView";
import { pageMetadata } from "@/lib/pages";
export function generateMetadata() { return pageMetadata("/"); }
export default function Home(){return <PageView path="/" />;}

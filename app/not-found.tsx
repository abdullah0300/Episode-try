import PageView from "@/components/PageView";
import { pageMetadata } from "@/lib/pages";
export function generateMetadata(){return pageMetadata("/404/");}
export default function NotFound(){return <PageView path="/404/" />;}

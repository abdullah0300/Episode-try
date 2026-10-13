import { notFound } from "next/navigation";
import PageView from "@/components/PageView";
import { routes, pageMetadata, type PagePath } from "@/lib/pages";
type Props = {params: Promise<{slug: string[]}>};
export const dynamicParams = false;
export function generateStaticParams(){return routes.filter(p=>p!=="/").map(p=>({slug:p.split("/").filter(Boolean)}));}
async function route({params}: Props): Promise<PagePath> {
  const path = "/" + (await params).slug.join("/") + "/";
  if (!routes.includes(path as PagePath)) notFound();
  return path as PagePath;
}
export async function generateMetadata(props: Props){return pageMetadata(await route(props));}
export default async function Page(props: Props){return <PageView path={await route(props)} />;}

import { pageComponents } from "@/lib/page-components";
import { pageData, type PagePath } from "@/lib/pages";
import SiteInteractions from "./SiteInteractions";
export default function PageView({path}: {path: PagePath}) {
  const Content = pageComponents[path];
  const graph = JSON.stringify(pageData(path).graph).replace(/</g, "\\u003c");
  return <><script type="application/ld+json" dangerouslySetInnerHTML={{__html: graph}} /><Content /><SiteInteractions /></>;
}

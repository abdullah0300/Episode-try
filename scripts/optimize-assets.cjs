const sharp = require('sharp');
const fs = require('fs');
(async () => {
 await sharp('public/assets/episode-journal-logo.png').resize({width:480}).webp({lossless:true}).toFile('public/assets/episode-journal-logo-480.webp');
 for (const file of fs.readdirSync('public/assets').filter(x=>/^(ep\d+|frame-\d+|hero)\.webp$/.test(x))) {
  const stem=file.slice(0,-5);
  for(const width of [480,960,1280]) await sharp('public/assets/'+file).resize({width,withoutEnlargement:true}).webp({quality:85}).toFile(`public/assets/${stem}-${width}.webp`);
 }
 console.log('Optimized logo bytes:',fs.statSync('public/assets/episode-journal-logo-480.webp').size);
})();

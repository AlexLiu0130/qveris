const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const rootDir = path.resolve(__dirname, '../..');
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1600, height: 1000 },
    deviceScaleFactor: 2
  });

  const filePath = path.resolve(rootDir, '06_deliverables/infographics/financial-data-capability-landscape.html');
  await page.goto(`file://${filePath}`);
  await page.screenshot({
    path: path.resolve(rootDir, '06_deliverables/infographics/financial-data-capability-landscape.png'),
    fullPage: true
  });

  await browser.close();
})();

browser.contextMenus.create({
    id: "opinionate-page",
    title: "Opinionate This Page"
  });
  
  browser.contextMenus.onClicked.addListener(function(info, tab) {
    if (info.menuItemId == "opinionate-page") {
      browser.tabs.executeScript({
        file: "opinionated.js"
      });
    }
  });
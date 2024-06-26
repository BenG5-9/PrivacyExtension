var text = document.getElementById("text");

var policySummary = "none";

console.log("run");

const setText = data => {
  var converter = new showdown.Converter();
  text.innerHTML = converter.makeHtml(data);
}

// on load
window.addEventListener('DOMContentLoaded', () => {
  
    // get active tab
    chrome.tabs.query({
      active: true,
      currentWindow: true
    }, tabs => {
      //
      chrome.tabs.sendMessage(
          tabs[0].id,
          {from: 'popup', subject: 'GetPolicy'},
          setText); // pass call back to content script
    });
  });
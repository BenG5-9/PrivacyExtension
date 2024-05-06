var curr_url = window.location.toString();
var curr_policy = "none";

chrome.runtime.sendMessage({
    from: 'content',
    subject: 'PolicyExtraction',
  });
  
// listen
chrome.runtime.onMessage.addListener((msg, sender, response) => {
  // validation
  if ((msg.from === 'popup') && (msg.subject === 'GetPolicy')) {
    
  // get the policy

  chrome.storage.local.get(["state"], (result)=>{
    console.log(result);
    if(Object.keys(result).length === 0)
    {
      $.ajax({
        type: "POST",
        headers: { 
            'Accept': 'application/json',
            'Content-Type': 'application/json' 
        },
        url: "http://localhost:8000/",
        data: JSON.stringify({url:curr_url}),
        success: (data)=>{
          curr_policy = data;
          chrome.storage.local.set({state:{data:curr_policy, url:curr_url}}).then(()=>response(curr_policy));
        }, // send the policy on completion
        error: (error)=>{console.log("Backend failed to obtain policy");response("Backend failed to obtain policy")},
        async:true
      });
      
    }
    else if(result.state.url != curr_url)
    {
      $.ajax({
        type: "POST",
        headers: { 
            'Accept': 'application/json',
            'Content-Type': 'application/json' 
        },
        url: "http://localhost:8000/",
        data: JSON.stringify({url:curr_url}),
        success: (data)=>{
          curr_policy = data;
          chrome.storage.local.set({state:{data:curr_policy, url:curr_url}}).then(()=>response(curr_policy));
        }, // send the policy on completion
        error: (error)=>{console.log("Backend failed to obtain policy");response("Backend failed to obtain policy")},
        async:true
      });
    }
    else
    {
      response(result.state.data);
    }
  });
  
}
return true;
});






// JAVASCRIPT IMPLEMENTATION

// var anchors = Array.from(document.getElementsByTagName('a')).filter((elem) => elem.innerHTML.match(/.*privacy.*/i) == elem.innerHTML);

// if(anchors[0] != null){
//     var link = anchors[0].href;
//     console.log(anchors[0].href);

//     // Get HTML from page
//     $.get( anchors[0].href.toString(), function( html ) {

//     // Loop through elements you want to scrape content from
//     $(html).find("p").each( function(){

//         var text = $(this).text();
//         console.log(text);
//         // Do something with content

//     } )
// } );
// }

// else{ //no policy page found
//     var link = "No policy page found";
//         console.log(text);
// }

// if (JOptionPane.showMessageDialog(null, "Here is the privacy page: ", link, JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE)
// == JOptionPane.YES_OPTION)
// {
//     null
// }
// else{
//     null
// }
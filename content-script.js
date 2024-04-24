
var curr_url = window.location.toString();

function callback(data)
{
    // This will eventually be the processed data
    console.log(data);
}

$.ajax({
    type: "POST",
    headers: { 
        'Accept': 'application/json',
        'Content-Type': 'application/json' 
    },
    url: "http://localhost:8000/",
    data: JSON.stringify({url:curr_url}),
    success: callback,
    async:false
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
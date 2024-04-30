var text = document.getElementById("text");

var policySummary = "none";

console.log("run");

while(policySummary == "none")
{
  $.get("http://localhost:8000/", (resp) => {
  })
  .done((resp)=>{console.log("Retrieval: " + resp)
    text.innerHTML = resp;})
  .fail((resp)=>{policySummary="No backend running.";text.innerHTML = policySummary;});
  break;
}

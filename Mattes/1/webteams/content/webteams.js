function confirmDelete_p (event_opl) {
	if ((event_opl.target.tagName.toLowerCase() == 'a') && (event_opl.target.className == "clDelete")) {
		
        if(confirm("Are you sure?")){
            alert("deleted")
        }else{
            event_opl.preventDefault();
		}
		// Klick auf Link zum L�schen
	}
}
function redirect() {
  window.location.replace("localhost:8089");
  return false;
}
window.onload = function () {
	let buttons = document.querySelectorAll("div.likeabutton");
	body_o[0].addEventListener('click', confirmDelete_p, false);
}

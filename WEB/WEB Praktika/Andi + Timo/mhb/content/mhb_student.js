var e = document.getElementById("studiengang");
var strUser = e.options[e.selectedIndex].value;

function studiengangAnzeige() {
		document.location.href = "/studiengang/" + strUser.toString();
}

window.onload=function(){
	let e = document.getElementById('studiengang');
	e.addEventListener('click', studiengangAnzeige, false);
}
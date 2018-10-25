function tabellen_event(event_opl){
		alert("juhu");
}
window.onload = function () {
    let tabelle = document.querySelectorAll("tr:nth-child(2)")[0];
    tabelle.addEventListener('click', tabellen_event , false);
}
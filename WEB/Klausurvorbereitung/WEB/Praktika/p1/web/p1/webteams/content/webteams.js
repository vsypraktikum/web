function confirmDelete_p (event_opl) {
	if ((event_opl.target.tagName.toLowerCase() == 'a') && (event_opl.target.className == "clDelete")) {
	// Klick auf Link zum Löschen

	
	// Ihre Ergänzung
		if (!confirm("Wollen Sie den Eintrag wirklich löschen?")){
			
			event_opl.preventDefault();
		}
	}

} 
window.onload = function () {
	let body_o = document.getElementsByTagName('body')[0]; 
	body_o.addEventListener('click', confirmDelete_p, false); 
}

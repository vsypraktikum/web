function form_abschicken(path) {
	var data = new FormData(document.getElementById("idWTForm"));
	console.log(data)
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("body").innerHTML =
			this.responseText;
		}
	};
	xhttp.open("POST", path, true);
	xhttp.send(data);
}
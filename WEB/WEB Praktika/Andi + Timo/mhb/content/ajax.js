function loadDocLogin() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("login").innerHTML = this.responseText;
		}
	};
	xhttp.open("GET", "loginLehrende.tpl", true);
  	.send();
}

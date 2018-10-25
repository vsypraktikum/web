function loadDocLogin() {
	var xhttp = new XMLHttpRequest();
	var username = document.getElementById("username").value;
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("login").innerHTML = this.responseText;
		}
	};
	xhttp.open("GET", "/login/?username=" + username, true);
  	xhttp.send();
}

function loadDocLoginL() {
	var xhttp = new XMLHttpRequest();
	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("loginL").innerHTML = this.responseText;
		}
	};
	xhttp.open("GET", "/loginL/?username=" + username + "&password=" + password, true);
  	xhttp.send();
}

function loadDoccreateStudiengang() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("formVerantwortlicherStudiengang").innerHTML = this.responseText;
		}
	};
	xhttp.open("GET", "/createStudiengang", true);
  	xhttp.send();
}

function loadDocstudiengangEdit() {
	var get = document.getElementById("studiengang");
	var selected = get.options[get.selectedIndex].value;
	if(selected == '0'){
		alert("Bitte geben Sie einen Studiengang an");
	}
	xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
			document.getElementById("formVerantwortlicherStudiengang").innerHTML = this.responseText;
		}
	};
	xhttp.open("GET", "/editStudiengang" + selected.toString(), true);
  	xhttp.send();
}





#!/bin/bash

function test {
	url="http://127.0.0.1:8080/$1"
	#rand=$(head -c 2 /dev/urandom)

	echo "$url"
	echo ""
	echo "$1 list"
	curl -s -S -f -G "$url" || echo "fail"
	echo ""
	echo ""
	echo "$1 new"
	tmp=""
	tmp=$(curl -s -S -f -X POST -d "$2$3$rand" "$url" || echo "fail")
	echo "$tmp"
	tmp=$(echo "$tmp" | grep -o -P "\d*")
	echo ""
	echo "$1 edit"
	curl -s -S -f -X PUT -d "$2$tmp$3" "$url"  || echo -e "fail"
	echo ""
	echo ""
	echo "$1 get"
	[ -n "$tmp" ] && (curl -s -S -f -G "$url$tmp" || echo -e "fail")
	[ -z "$tmp" ] && echo -e "skip"
	echo ""
	echo ""
	echo "$1 delete"
	[ -n "$tmp" ] && (curl -s -S -f -X DELETE -d "$2$3" "$url$tmp" || echo -e "fail")
	[ -z "$tmp" ] && echo -e "skip"	
	echo ""
	echo ""
}

function get {
	url="http://127.0.0.1:8080/$1"
	#echo "$url"
	echo "$1"
	curl -s -S -G "$url" || echo "fail"
	echo ""
	echo ""
}

rand=abc

echo "rest test script"
echo ""


test projekt/ "id_s=" "&name_s=$rand"
#kein fehler DELETE
test fehler/ "id_s=" "&komponente_s=$rand&beschreibung_s=$rand&mitarbeiter_s=$rand&datum_s=$rand&kategorie_s=$rand&fehlerstatus_s=$rand"
get fehler/?type=erkannt
get fehler/?type=behoben
#projektkomponenten:id
test komponente/ "id_s=" "&name_s=$rand&beschreibung_s=$rand&projekt_s=$rand"
#qsmitarbeiter 4x
#swentwickler 4x
#katursache 4x
#prolist
get prolist/
#katlist
get katlist/
#template
get templates/

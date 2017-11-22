 <h1>Teilnahmen</h1>

<table id="table_teilnahme">
    <tr><th>Name</th><th>Status</th></tr>

    %for key_s in data_o:
    <tr id="r${key_s}"><td>${data_okey_s'name'},${data_okey_s'vorname'}</td><td>${data_okey_s'status'}</td></tr>
    %endfor
</table>
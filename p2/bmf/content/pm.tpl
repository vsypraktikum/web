﻿
            <h1>Pflege Mitarbeiter</h1>
<ul>
    % for key_s in data_o:
    <li id="r${key_s}">${data_okey_s 'name'},${data_okey_s'vorname'}</li>
    <a href=""> Anzeigen </a>
    <a href=""> Ändern </a>
    %endfor
</ul>

<input type="submit" value="Erfassen" />


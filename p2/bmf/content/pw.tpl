
            <h1>Pflege Weiterbildungen</h1>
<ul>
    % for key_s in data_o:
    <li id="r${key_s}">${data_okey_s 'weiterbildung'}</li>
    <a href=""> Anzeigen </a>
    <a href=""> �ndern </a>
    %endfor
</ul>

<input type="submit" value="Erfassen" />
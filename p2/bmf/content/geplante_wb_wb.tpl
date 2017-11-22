% if weiterbildung[7] == 'laufend'
<h2>geplant:</h2>
<ul>
	% for key_s in data_o:
	<li id="r${key_s}">${data_okey_s 'bz_w'}</li>
	%endfor
</ul>
%endif
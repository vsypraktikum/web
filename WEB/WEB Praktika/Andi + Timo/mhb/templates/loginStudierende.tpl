<%inherit file="layout.tpl" />
<%block name="header">
	<body>
		<div id="login">
			<form id="formlogin" action="" method="POST">
				<input type="text" id="username" name="username" value="" required />
				<button onclick="loadDocLogin()">Login</button>
			</form>
		</div>
	</body>
</%block>

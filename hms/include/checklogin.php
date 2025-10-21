<?php
function check_login()
{
	if (strlen($_SESSION['login']) == 0) {
		$host = $_SERVER['HTTP_HOST'];
		$uri  = rtrim(dirname($_SERVER['PHP_SELF']), '/\\');
		$extra = "./user-login.php";
		header("Location: http://$host$uri/$extra");
	}
}
// This function checks if the user is logged in, if not, it redirects to the login page.
?>

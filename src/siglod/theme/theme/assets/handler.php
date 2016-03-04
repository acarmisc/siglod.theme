<?php
header('Content-Type: text/html; charset=utf-8');

if ( isset($_POST['sbmt'])  ) {
	if ( !empty($_POST['user_name']) && !empty($_POST['email']) && !empty($_POST['user_message']) ) {
		$admin_email    = 'youremail@email.com';
		$subject 		= $_POST['user_name'];
		$message 		= $_POST['user_message'];
		$headers 		= 'From: '.$_POST['email'];
		
		mail($admin_email, $subject, $message, $headers);
		
		echo 1;
	}
	else {
		echo 0;
	}
}
else {
	echo 0;
}
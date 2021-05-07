<?php

	$data = $_POST['data'];
	$f = fopen('data.json', 'w+');
	$r = fwrite($f, $data);
	fclose($f);
	if ($r) echo "success";

?>
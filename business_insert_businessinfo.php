<?php
	

    $db =  mysqli_connect('localhost:3306', 'staffmember', 'Customer1');
	mysqli_select_db($db, 'business_info');
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }	
	
    $query= "INSERT INTO clientinfo (salut, firstname, mid_init, lastname, suffix, title, company_name, department, address1, address2, suite_no, city, state, postal_code, zip_code, mobile_phone, office_phone, home_phone, fax_phone, office_email, home_email, gender, age, notes) values('$_POST[salut]', '$_POST[firstname]', '$_POST[mid_init]', '$_POST[lastname]', '$_POST[suffix]', '$_POST[title]', '$_POST[company_name]', '$_POST[department]', '$_POST[address1]', '$_POST[address2]', '$_POST[suite_no]', '$_POST[city]', '$_POST[state]', '$_POST[postal_code]', '$_POST[zip_code]', '$_POST[mobile_phone]', '$_POST[office_phone]', '$_POST[home_phone]', '$_POST[fax_phone]', '$_POST[office_email]', '$_POST[home_email]', '$_POST[gender]', '$_POST[age]', '$_POST[notes]')";
	   
    mysqli_query($db, $query);
 



	// echo '<form action="first_record.php" method="post"><input type="submit" name="submit" value="First Record"></form>';
	header("refresh:1; url=business_last_record.php");
?>
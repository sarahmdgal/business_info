<!DOCTYPE html>
<html>
<head>
<script type="text/javascript">
	label {
	cursor: pointer;
	color: "#E387AA;"
	display: block;
	padding: 10px;
	margin: 3px;
	}
	function ClearPlaceHolder (input) {
		input.defaultValue==""
		if (input.value == input.defaultValue) {
			input.value = "";
		}
	}
	function SetPlaceHolder (input) {
		if (input.value == "") {
			input.value = input.defaultValue;
		}
	}
	 function submitForm(action) {
		var form = document.getElementById('customer_data_results.php');
		form.action = action;
		form.submit();
</script>
  <title>Customer Data Search Results</title>
</head>
<body bgcolor="#ce0f69">
  <h1><font color="E387AA"><center>Customer Data Search Results</center></font></h1>
	<?php

	
    $db = mysqli_connect('localhost:3306', 'root', 'Y@nkees1!');
	mysqli_select_db($db, 'customerservice');

	
/* 		$salut=$_POST['salut'], 
		$firstname=$_POST[firstname],
		$mid_init = '$_POST[mid_init], 
		$lastname = '$_POST[lastname], 
		$suffix = '$_POST[suffix], 
		$title =$_POST[title], 
		$company_name = '$_POST[company_name], 
		$department = '$_POST[department], 
		$address1 = '$_POST[address1], 
		$address2 = '$_POST[address2], 
		$suite_no = '$_POST[suite_no], 
		$city =$_POST[city], 
		$state =$_POST[state], 
		$postal_code =$_POST[postal_code], 
		$zip_code = '$_POST[zip_code], 
		$mobile_phone = '$_POST[mobile_phone], 
		$office_phone = '$_POST[office_phone], 
		$home_phone = '$_POST[home_phone], 
		$fax_phone = '$_POST[fax_phone], 
		$office_email = '$_POST[office_email], 
		$home_email = '$_POST[home_email], 
		$gender = '$_POST[gender], 
		$age = '$_POST[age], 
		$notes  = '$_POST[notes]'  
		$PersonID = '$_POST[PersonID]'; 
		
		print($salut);
		print($firstname);
		print($mid_init);
		print($lastname);
		print($mobile_phone);
		print($office_phone);
		print($home_phone);
		print($fax_phone);
		print($office_email);
	 */
	
		$query = "UPDATE person SET 
		salut='$_POST[salut]', 
		firstname='$_POST[firstname]',
		mid_init = '$_POST[mid_init]', 
		lastname = '$_POST[lastname]', 
		suffix = '$_POST[suffix]', 
		title ='$_POST[title]', 
		company_name = '$_POST[company_name]', 
		department = '$_POST[department]', 
		address1 = '$_POST[address1]', 
		address2 = '$_POST[address2]', 
		suite_no = '$_POST[suite_no]', 
		city ='$_POST[city]', 
		state ='$_POST[state]', 
		postal_code ='$_POST[postal_code]', 
		zip_code = '$_POST[zip_code]', 
		mobile_phone = '$_POST[mobile_phone]', 
		office_phone = '$_POST[office_phone]', 
		home_phone = '$_POST[home_phone]', 
		fax_phone = '$_POST[fax_phone]', 
		office_email = '$_POST[office_email]', 
		home_email = '$_POST[home_email]', 
		gender = '$_POST[gender]', 
		age = '$_POST[age]', 
		notes  = '$_POST[notes]'  
		WHERE PersonID = '$_POST[PersonID]'"; 

		if (mysqli_query($db, $query))
			header("refresh:1; url=first_record.php");
		else
			echo "Record was not updated."

	// mysqli_commit;

		
		
		
		
		
		
		

	?>
</body>
</html>
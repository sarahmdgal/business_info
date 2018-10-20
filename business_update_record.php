<!DOCTYPE html>
<html>
<head>
<style>
.frm-group form {
    background-color: #C1B7BB; /* Gray background */
    border: 1px solid black; /* black border */
    color: white; /* White text */
    padding: 10px 24px; /* Some padding */
    cursor: pointer; /* Pointer/hand icon */
    float: left; /* Float the buttons side by side */
}

/* Clear floats (clearfix hack) */
.frm-group:after {
    content: "";
    clear: both;
    display: table;
}

.frm-group form:not(:last-child) {
    border-right: none; /* Prevent double borders */
}

/* Add a background color on hover */
.frm-group form:hover {
    background-color: #0045B0;
}
</style>
    <script type="text/javascript">
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
			var form = document.getElementById('form1');
			form.action = action;
			form.submit();
    </script>
  <title>Business Customer Information Screen</title>
</head>
<body bgcolor="#C3B7BC">
  <h1><font color="071D49"><center>Business Customer Information Screen</center></font></h1>
	<?php

	
    $db = mysqli_connect('localhost:3306', 'staffmember', 'Customer1');
	mysqli_select_db($db, 'business_info');

	
	
		$query = "UPDATE clientinfo SET 
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
		company_website = '$_POST[company_website]',	
		gender = '$_POST[gender]', 
		age = '$_POST[age]', 
		notes  = '$_POST[notes]'  
		WHERE PersonID = '$_POST[PersonID]'"; 

		if (mysqli_query($db, $query))
			header("refresh:1; url=business_first_record.php");
		else
			echo "Record was not updated."
    //$db->close();

	?>
</body>
</html>
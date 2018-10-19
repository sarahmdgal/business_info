<!DOCTYPE html>
<html>
<head>
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
  <title>Customer Data Search Results</title>
</head>

<body bgcolor="#ce0f69">
  <h1><font color="E387AA"><center>Customer Data Search Results</center></font></h1>
  <?php  
	  echo '<form action="insert_customerservice.php" method="post">
	  <p><strong>Salut:&nbsp;&nbsp;<input name="salut" type="text" size="3">&nbsp;&nbsp;&nbsp;First Name:&nbsp;&nbsp;<input name="firstname" type="text" size="15">&nbsp;&nbsp;&nbsp;Mid Init:&nbsp;&nbsp;<input name="mid_init" type="text" size="15">&nbsp;&nbsp;&nbsp;Last Name:&nbsp;&nbsp;<input name="lastname" type="text" size="15">&nbsp;&nbsp;&nbsp;Suffix:&nbsp;&nbsp;<input name="suffix" type="text" size="5"></p></strong>
	  <p><strong>Job Title:&nbsp;&nbsp;<input name="title" type="text" size="50"></p></strong>
	  <p><strong>Company Name:&nbsp;&nbsp;<input name="company_name" type="text" size="60">&nbsp;&nbsp;&nbsp;Department:&nbsp;&nbsp;<input name="department" type="text" size="40"></p></strong>
	  <p><strong>Address1:&nbsp;&nbsp;<input name="address1" type="text" size="50">&nbsp;&nbsp;&nbsp;Address2:&nbsp;&nbsp;<input name="address2" type="text" size="25">&nbsp;&nbsp;&nbsp;Suite No.:&nbsp;&nbsp;<input name="suite_no" type="text" size="10"></p></strong>
	  <p><strong>City:&nbsp;&nbsp;<input name="city" type="text" size="25">&nbsp;&nbsp;&nbsp;State:&nbsp;&nbsp;<input name="state" type="text" size="5">&nbsp;&nbsp;&nbsp;Postal Code:&nbsp;&nbsp;<input name="postal_code" type="text" size="15">&nbsp;&nbsp;&nbsp;Zip Code:&nbsp;&nbsp;<input name="zip_code" type="text" size="15"></p></strong>
	  <p><strong>Mobile Phone:&nbsp;&nbsp;<input name="mobile_phone" type="text" size="15">&nbsp;&nbsp;&nbsp;Office Phone:&nbsp;&nbsp;<input name="office_phone" type="text" size="15">&nbsp;&nbsp;&nbsp;Home Phone:&nbsp;&nbsp;<input name="home_phone" type="text" size="15">&nbsp;&nbsp;&nbsp;Fax Phone:&nbsp;&nbsp;<input name="fax_phone" type="text" size="15"></p></strong>
	  <p><strong>Office Email:&nbsp;&nbsp;<input name="office_email" type="text" size="50">&nbsp;&nbsp;&nbsp;Home Email:&nbsp;&nbsp;<input name="home_email" type="text" size="50"></p></strong>
	  <p><strong>Gender:&nbsp;&nbsp;<input name="gender" type="text" size="10">&nbsp;&nbsp;&nbsp;Age:&nbsp;&nbsp;<input name="age" type="text" size="3">&nbsp;&nbsp;&nbsp;Notes:&nbsp;&nbsp;<input name="notes" type="text" size="100"></p></strong>
	  <p></strong><input type="submit" name="submit" value="Insert New Record"></p></strong>
	  </form>';
	  
	  

	  
	  
	  
	  

  ?>
</body>
</html>
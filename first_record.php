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
    $db =  mysqli_connect('localhost:3306', 'root', 'Y@nkees1!', 'customerservice');
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }

		$query = "SELECT * FROM person WHERE PersonID IN (SELECT min(PersonID) FROM person)";
		$result = mysqli_query($db, $query);
		
		while($row=mysqli_fetch_assoc($result))
		{
			echo "<form action='update_record.php' method=post>"; 
			echo '<p><strong><label for="PersonID">Person ID:</label>&nbsp;&nbsp;<input name="PersonID" type="text" size="3" value="'.$row['PersonID'].'"></strong></p>';			
			echo '<p><strong><label for="salut">Salut:</label>&nbsp;&nbsp;<input name="salut" type="text" size="5" value="'.$row['salut'].'">
			<label for="firstname">First Name:</label>&nbsp;&nbsp;<input name="firstname" type="text" size="15" value="'.$row['firstname'].'">
			<label for="mid_init">Mid Init:</label>&nbsp;&nbsp;<input name="mid_init" type="text" size="5" value="'.$row['mid_init'].'">
			<label for="lastname">Last Name:</label>&nbsp;&nbsp;<input name="lastname" type="text" size="15" value="'.$row['lastname'].'">
			<label for="suffix">Suffix:</label>&nbsp;&nbsp;<input name="suffix" type="text" size="5" value="'.$row['suffix'].'"></strong></p>';
			echo '<p><strong><label for="title">Job Title:</label>&nbsp;&nbsp;<input name="title" type="text" size="40"  value="'.$row['title'].'"></p></strong>';
			echo '<p><strong><label for="company_name">Company Name:</label>&nbsp;&nbsp;<input name="company_name" type="text" size="50"  value="'.$row['company_name'].'"><label for="department">Department:</label>&nbsp;&nbsp;<input name="department" type="text" size="40"  value="'.$row['department'].'"></strong></p>';
			echo '<p><strong><label for="address1">Address1:</label>&nbsp;&nbsp;<input name="address1" type="text" size="40"  value="'.$row['address1'].'">
			      <label for="address2">Address2:</label>&nbsp;&nbsp;<input name="address2" type="text" size="25"  value="'.$row['address2'].'">
			      <label for="suite_no">Suite No.:</label>&nbsp;&nbsp;<input name="suite_no" type="text" size="15"  value="'.$row['suite_no'].'"></strong></p>';
			echo '<p><strong><label for="city">City:</label>&nbsp;&nbsp;<input name="city" type="text" size="25"  value="'.$row['city'].'">
			<label for="state">State:</label>&nbsp;&nbsp;<input name="state" type="text" size="5"  value="'.$row['state'].'">
			<label for="postal_code">Postal Code:</label>&nbsp;&nbsp;<input name="postal_code" type="text" size="15" value="'.$row['postal_code'].'">
			<label for="zip_code">Zip Code:</label>&nbsp;&nbsp;<input name="zip_code" type="text"  size="15" value="'.$row['zip_code'].'"></strong></p>';
			echo '<p><strong<label for="mobile_phone">Mobile Phone:</label>&nbsp;&nbsp;<input name="mobile_phone" type="text" size="15" value="'.$row['mobile_phone'].'">
			<label for="office_phone">Office Phone:</label>&nbsp;&nbsp;<input name="office_phone" type="text" size="15"  value="'.$row['office_phone'].'">
			<label for="home_phone">Home Phone:</label>&nbsp;&nbsp;<input name="home_phone" type="text" size="15"  value="'.$row['home_phone'].'">
			<label for="fax_phone">Fax Phone:</label>&nbsp;&nbsp;<input name="fax_phone" type="text" size="15" value="'.$row['fax_phone'].'"></strong></p>';
			echo '<p><strong><label for="office_email">Office Email:</label>&nbsp;&nbsp;<input name="office_email" type="text" size="50" value="'.$row['office_email'].'">
			<label for="home_email">Home Email:</label>&nbsp;&nbsp;<input name="home_email" type="text" size="50" value="'.$row['home_email'].'"></strong></p>';
			echo '<p><strong><label for="gender">Gender:</label>&nbsp;&nbsp;<input name="gender" type="text" size="10"  value="'.$row['gender'].'">
			<label for="age">Age:</label>&nbsp;&nbsp;<input name="age" type="text" size="5"  value="'.$row['age'].'"><label for="notes">Comments/Notes:</label>&nbsp;&nbsp;<input name="notes" type="text" size="100" value="'.$row['notes'].'"></strong></p>';
			echo '<input type="submit" name="Update Record">';
			echo "</form>";
		
			echo '<form action="add_new_record.php" method="post"><input type="submit" name="submit" value="Add New Record"></form>
				  <form action="first_record.php" method="post"><input type="submit" name="submit" value="First Record"></form>
				  <form action="previous_record.php" method="post"><input name="searchterm" type="hidden" size="5" value='.$row['PersonID'].'><input type="submit" name="submit" value="Previous Record"></form>
				  <form action="next_record.php" method="post"><input name="searchterm" type="hidden" size="5" value='.$row['PersonID'].'><input type="submit" name="Next Record" value="Next Record"></form>
				  <form action="last_record.php" method="post"><input type="submit" name="submit" value="Last Record"></form>';

			echo '<form action="delete_record.php" method="post"><input name="searchterm" type="hidden" size="5" value='.$row['PersonID'].'><input type="submit" name="submit" value="Delete Record"></form>';		
		}
	$result->free_result();
    $db->close();
  ?>
  </body>
 </html> 
<!DOCTYPE html>
<html>
<head>
<style>
.frm-group form {
    background-color: #C1B7BB; /* Green background */
    border: 1px solid green; /* Green border */
    color: white; /* White text */
    padding: 10px 24px; /* Some padding */
    cursor: pointer; /* Pointer/hand icon */
    float: left; /* Float the buttons side by side */
}

/* Clear floats (clearfix hack) */
.btn-group:after {
    content: "";
    clear: both;
    display: table;
}

.frm-group form:not(:last-child) {
    border-right: none; /* Prevent double borders */
}

/* Add a background color on hover */
.frm-group form:hover {
    background-color: #3e8e41;
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

	$searchterm=$_POST['searchterm'];

	
    $db =  mysqli_connect('localhost:3306', 'staffmember', 'Customer1');
	mysqli_select_db($db, 'business_info');
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }

		$query = "DELETE FROM clientinfo WHERE PersonID = $searchterm";
		$result = mysqli_query($db, $query);
		
	// $result->free_result();
    $db->close();
    $db =  mysqli_connect('localhost:3306', 'staffmember', 'Customer1');
	mysqli_select_db($db, 'business_info');
	
	
	
	
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }
		$query = "ALTER TABLE clientinfo DROP COLUMN PersonID";
		$result = mysqli_query($db, $query);
	
	// $result->free_result();
    $db->close();
	
    $db =  mysqli_connect('localhost:3306', 'staffmember', 'Customer1');
	mysqli_select_db($db, 'business_info');
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }

		$query = "ALTER TABLE clientinfo ADD PersonID INT NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST";
		$result = mysqli_query($db, $query);
		
	// $result->free_result();
    $db->close();
	
    $db =  mysqli_connect('localhost:3306', 'staffmember', 'Customer1');
	mysqli_select_db($db, 'business_info');
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }
		$query = "SELECT * FROM clientinfo";
		$result = mysqli_query($db, $query);
	$result->free_result();
    $db->close();

	// echo '<form action="first_record.php" method="post"><input type="submit" name="submit" value="First Record"></form>';
	header("refresh:1; url=business_first_record.php");
	

	
  ?>



</body>
 </html> 
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
  <title>Business Customer Information Screen</title>
</head>
<body bgcolor="#ce0f69">
  <h1><font color="E387AA"><center>Business Customer Information Screen</center></font></h1>
  <?php

	$searchterm=$_POST['searchterm'];

	
    $db =  mysqli_connect('localhost:3306', 'staffmember', 'Customer1');
	mysql_select_db($db, 'business_info');
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
	mysql_select_db($db, 'business_info');	
	
	
	
	
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
	mysql_select_db($db, 'business_info');
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
	mysql_select_db($db, 'business_info');
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
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

	$searchterm=$_POST['searchterm'];

	
    $db =  mysqli_connect('localhost:3306', 'root', 'Y@nkees1!', 'customerservice');
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }

		$query = "DELETE FROM person WHERE PersonID = $searchterm";
		$result = mysqli_query($db, $query);
		
	// $result->free_result();
    $db->close();
    $db =  mysqli_connect('localhost:3306', 'root', 'Y@nkees1!', 'customerservice');
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }
		$query = "ALTER TABLE person DROP COLUMN PersonID";
		$result = mysqli_query($db, $query);
	
	// $result->free_result();
    $db->close();
	
	
	
    $db =  mysqli_connect('localhost:3306', 'root', 'Y@nkees1!', 'customerservice');
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }

		$query = "ALTER TABLE person ADD PersonID INT NOT NULL PRIMARY KEY AUTO_INCREMENT FIRST";
		$result = mysqli_query($db, $query);
		
	// $result->free_result();
    $db->close();
	
    $db =  mysqli_connect('localhost:3306', 'root', 'Y@nkees1!', 'customerservice');
    if (mysqli_connect_errno()) {
       echo '<p>Error: Could not connect to database.<br/>
       Please try again later.</p>';
       exit;
    }

		$query = "SELECT * FROM person";
		$result = mysqli_query($db, $query);
	$result->free_result();
    $db->close();

	// echo '<form action="first_record.php" method="post"><input type="submit" name="submit" value="First Record"></form>';
	header("refresh:1; url=first_record.php");
	

	
  ?>



</body>
 </html> 
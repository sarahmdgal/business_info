<!DOCTYPE html>
<html>
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
  <title>Business Customer Information Search Screen</title>
</head>
<body bgcolor="#C3B7BC">
  <h1><font color="071D49"><center>Business Customer Information Search Screen</center></font></h1>
  <?php  
	  echo '<form action="business_search_results.php" method="post">
	  <p><strong>&nbsp;&nbsp;&nbsp;First Name:&nbsp;&nbsp;<input name="firstname" type="text" size="15"></strong></p>
	  <p><strong>&nbsp;&nbsp;&nbsp;Last Name:&nbsp;&nbsp;<input name="lastname" type="text" size="15"></strong></p>
	  <input type="submit" name="submit" value="Find Record"></form>';
	  
	  

	  
	  
	  
	  

  ?>
</body>
</html>
<!DOCTYPE html>
<html>
<head>
	<title>Lokaverkefni</title>
</head>
<body>
	%for x in result:
		
	<br>
	{{x['PlateNumber']}}<br>
	{{x['Manufacturer']}}<br>
	{{x['Model']}}<br>
	%end	
	<br>
	<form method="POST" action="/sina" accept-charset="ISO-8859-1">
      bílnúmer:<br>
      <input type="text" name="bilnumer"><br>
      <input type="submit" href="./sina">
  </form> 

</body>
</html>
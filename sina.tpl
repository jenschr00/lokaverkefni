<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form method='POST' action="/kaupa" accept-charset="ISO-8859-1">
		%for x in result:
			<br>
			{{x['PlateNumber']}}<br>
			{{x['Manufacturer']}}<br>
			{{x['Model']}}<br>
			{{x['Color']}}<br>
			{{x['Car_Name']}}<br>
			{{x['Man_Year']}}<br>
			{{x['Price']}}<br>
			<input type="radio" name="PlateNumber" value="{{x['PlateNumber']}}">
		%end
	<input type="submit" href="./kaupa" value="Kaupa">
	</form>
</body>
</html>
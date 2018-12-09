<!DOCTYPE html>
<html>
<head>
	<title>Lokaverkefni</title>
</head>
<body>
    %for i in results:
        {{i['User_id']}}<br>
        {{i['Car_Number']}}<br>
        {{i['Car_Price']}}<br>
        {{i['Order_Date']}}<br>
    %end
</body>
</html>
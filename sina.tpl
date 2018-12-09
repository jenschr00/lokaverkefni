<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="/static/skeleton.css">
</head>
<body class="blackback">
    <a class="button" href="/">Home</a>
	<form method='POST' action="/kaupa" accept-charset="ISO-8859-1">
		<table class="u-full-width">
    <thead>
    <tr>
    %count = 1
    %for i in results:
        %if count == 1:
        %for x in i:
            <th styles="padding:20px;  text-align:center;">{{x}}</th>
        %end
        %end
    %count += 1
    %end
    <th styles="padding:20px;  text-align:center;">Kaupa</th>
    </tr>
    </thead>
    <tbody>
    %for i in results:
        <tr>
            <td styles="text-align:center;">{{i['PlateNumber']}}</td>
            <td styles="text-align:center;">{{i['Color']}}</td>
            <td styles="text-align:center;">{{i['Manufacturer']}}</td>
            <td styles="text-align:center;">{{i['Model']}}</td>
            <td styles="text-align:center;">{{i['Sjalfskiptur']}}</td>
            <td styles="text-align:center;">{{i['Beinskiptur']}}</td>
            <td styles="text-align:center;">{{i['Car_Name']}}</td>
            <td styles="text-align:center;">{{i['Man_Year']}}</td>
            <td styles="text-align:center;">{{i['Price']}}</td>
            <td><input type="radio" name="PlateNumber" value="{{i['PlateNumber']}}" required></td>
        </tr>
    %end
    </tbody>
</table>
	<input type="submit" href="./kaupa" value="Kaupa">
	</form>
</body>
</html>
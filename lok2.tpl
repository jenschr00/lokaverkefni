<!DOCTYPE html>
<html>
<head>
	<title>Lokaverkefni</title>
	<link rel="stylesheet" type="text/css" href="/static/skeleton.css">
</head>
<body class="blackback">
<a class="button" href="/">Home</a>
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
    </tr>
    </thead>
    <tbody>
    %for i in results:
        <tr>
            <td styles="text-align:center;">{{i['User_id']}}</td>
            <td styles="text-align:center;">{{i['Car_Number']}}</td>
            <td styles="text-align:center;">{{i['Car_Price']}}</td>
            <td styles="text-align:center;">{{i['Order_Date']}}</td>
        </tr>
    %end
    </tbody>
</table>
</body>
</html>
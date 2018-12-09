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
        <th>BílNúmer</th>
        <th>Tegund</th>
        <th>UndirTegund</th>
        <th>ÁrGerð</th>
    </tr>
    </thead>
	<tbody>
    %for i in results:
        <tr>
            <td styles="text-align:center;">{{i['PlateNumber']}}</td>
            <td styles="text-align:center;">{{i['Manufacturer']}}</td>
            <td styles="text-align:center;">{{i['Model']}}</td>
            <td styles="text-align:center;">{{i['Man_Year']}}</td>
        </tr>
    %end
    </tbody>
</table>
	<form method="POST" action="/sina" accept-charset="ISO-8859-1">
      bílnúmer:<br>
      <input type="text" name="bilnumer" required><br>
      <input type="submit" href="./sina">
  </form> 

</body>
</html>
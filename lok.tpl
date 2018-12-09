<!DOCTYPE html>
<html>
<head>
<title>Lokaverkefni</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="./static/normalize.css">
  <link rel="stylesheet" type="text/css" href="./static/CSS.css">


</head>
<body>
  <div class="parallax">
    <h1>Jens og Friðrik</h1>

    <h3>Lokaverkefnið okkar</h3>
  </div>

  <div class="glæra1">
    %if data['Usertype'] == '':
        <h3>Skráðu þig inn fyrir valmöguleika</h3>
    %elif data['Usertype'] == 'Admin':
        <a href="/solur">Seldir Bílar</a><br>
        <a href="/skoda">Kaupa Bíl</a><br>
        <a href="/selja">Selja Bíl</a><br>
    %else:
        <a href="/skoda">Kaupa Bíl</a><br>
        <a href="/selja">Selja Bíl</a><br>
    %end

  </form> 
  </div>

  <div class="parallax2">
  </div>

  <div class="glæra2">
    %if data['User'] == '':
        <a class="button" href="login" style="display: inline-block;">Login</a>
    %else:
        <a href="/logout">Logout</a>
    %end
  <a class="button" href="Signup" style="display: inline-block;">Signup</a>
  </div>
      
 

</body>
</html>
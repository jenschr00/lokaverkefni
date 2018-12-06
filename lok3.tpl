<!DOCTYPE html>
<html>
<head>
	<title>Lokaverkefni</title>
</head>
<body>
	<form method="POST" action="/sqlimport" accept-charset="ISO-8859-1">
		<input type="text" name="nafn" placeholder="Fullt Nafn" required><br>
		<input type="text" name="bilnumer" placeholder="Bílnúmer" required><br>
		<input type="text" name="tegund" placeholder="Tegund" required><br>
		<input type="text" name="undirtegund" placeholder="Undirtegund" required><br>
		 <input type="text" name="litur" placeholder="Litur" required><br>
		Sjálfskipting <input type="radio" id="Sjálfskiptur" name="skipting" value="Sjálfskiptur"><br>
		Beinskipting <input type="radio" id="Beinskiptur" name="skipting" value="Beinskiptur"><br>
		<input type="text" name="argerd" placeholder="Árgerð" required><br>
		<input type="text" name="verd" placeholder="Verð" required><br>
		<input type="submit" value="Selja" href="/sqlimport" required>
	</form>
</body>
</html>
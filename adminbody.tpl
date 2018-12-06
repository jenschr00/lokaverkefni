<h3 class="u-full-width" style="text-align:center;">
	Admin
</h3>
<a href="/" class="button">Signout</a>
<table class="u-full-width" style="align-items:center;">
	<thead>
		<tr>
			<th style="text-align:center; border-right: 0.1px solid lightgrey;">UserNames</th>
			<th style="text-align:center; border-right: 0.1px solid lightgrey;">Name</th>
			<th style="text-align:center; border-right: 0.1px solid lightgrey;">PassWD</th>
		</tr>
	</thead>
	<tbody>
		%for i in data:
		<tr>
			%for x in i:
			<td style="text-align:center; border-right: 0.1px solid lightgrey;">{{x}}</td>
			%end
		</tr>
		%end
	</tbody>
</table>
% rebase('layout.tpl', way=way, year=year)

<h2>{{ way }}.</h2>
<h3>{{ message }}</h3>

<p>Use this area to provide additional information.</p>
%if member:
<p>{{member.role}}</p>
<p>{{member.name}}</p>
<p>{{member.nick}}</p>
<p>{{member.password}}</p>
<p>{{member.regdate}}</p>
<p>{{member.active}}</p>
%end
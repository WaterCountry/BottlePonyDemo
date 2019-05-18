% rebase('layout.tpl', way=way, year=year)

<h2>{{ way }}.</h2>
<h3>{{ message }}</h3>

<p>Use this area to provide additional information.</p>
<h1>{{ arts }}</h1>

<ul>
    % for title in arts:
      <li>{{ title }}</li>
    % end
</ul>
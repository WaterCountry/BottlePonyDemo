% rebase('layout.tpl', way=way, year=year)

<h2>{{ way }}.</h2>
<h3>{{ message }}</h3>

<p>Use this area to provide additional information.</p>


<ul>
    % for title in arts:
      <li>{{ title }}</li>
    % end
</ul>

<table class="table table-striped">
    <thead>
        <tr>
            <th></th>
            <th>标题</th>
            <th>发布</th>
            <th>日期</th>
            <th>作者</th>
        </tr>
    </thead>
    <tbody>
        % for t in arts:
        <tr>
            <td>{{t.id}}</td>
            <td>{{t.title}}</td>
            <td>{{t.publish}}</td>
            <td>{{t.update}}</td>
            <td>{{t.author}}</td>
        </tr>
        % end
    </tbody>
</table>
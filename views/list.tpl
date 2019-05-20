% rebase('layout.tpl', way=way, year=year)

<h2>{{ way }}.</h2>
<h3>{{ message }}</h3>

<p>Use this area to provide additional information.</p>

<div class="container">
    <div class="row">
        <div class="">
            <a href="/add">添加文章</a>
        </div>
    </div>
<div class="row">

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
            <td><a href='/article/{{ t.id }}'>{{t.title}}</a> </td>
            <td>{{t.publish}}</td>
            <td>{{t.update}}</td>
            <td>{{t.author}}</td>
        </tr>
        % end
    </tbody>
</table>
</div>

<div class="row">
    <nav aria-label="Page navigation">
              <ul class="pagination">
                <li>
                  <a href="#" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                  </a>
                </li>
                  %for i in range(5):
                    <li><a href="#">{{ i }}</a></li>
                  %end

                <li>
                  <a href="#" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                  </a>
                </li>
              </ul>
            </nav>
</div>

</div>
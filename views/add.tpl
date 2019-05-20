% rebase('layout.tpl', way=way, year=year)

<h2>{{ way }}.</h2>
<h3>{{ message }}</h3>

<div class="container">

<div class="row">

    <form action="/add" method="post"  class="form-horizontal">
      <div class="form-group">
        <label for="title" class="col-sm-4 control-label">标题</label>

        <div class="col-sm-8">
          <input type="text" class="form-control" name="title" placeholder="title">
        </div>
      </div>
      <div class="form-group">
        <label for="content" class="col-sm-4 control-label">内容</label>

        <div class="col-sm-8">
          <input type="text" class="form-control" name="content" placeholder="content">
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-6 col-sm-6">
          <button type="submit" class="btn btn-default ">添加文章</button>
        </div>
      </div>
    </form>

</div>

</div>
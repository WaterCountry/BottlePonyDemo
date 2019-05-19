% rebase('layout.tpl', way=way, year=year)

<h2>{{ way }}.</h2>
<h3>{{ message }}</h3>

<div class="container">

<div class="row">
      <form action="/login" method="post" class="form-signin">
        <h2 class="form-signin-heading">Please sign in</h2>
        <label for="id_username" class="sr-only">账号</label>
        <input type="text"  name="username" class="form-control" placeholder="Email address" required autofocus>
        <label for="id_password" class="sr-only">密码</label>
        <input type="password" name="password" class="form-control" placeholder="Password" required>
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me"> 记住我
          </label>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit">登录</button>
      </form>

</div><br>
<div class="row">
    <div class="form-group">
                        没有账号？
                     <a href="/register" title="" class="btn btn-primary">立即注册</a>
    </div>
</div>
</div> <!-- /container -->


</div>
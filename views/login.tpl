% rebase('layout.tpl', way=way, year=year)

<h2>{{ way }}.</h2>
<h3>{{ message }}</h3>

<div class="row">
    <div class="col-md-12">
        <section id="loginForm">
            <form action="/login" method="GET" class="form-horizontal">
                <h4>请使用本地账号登录</h4>
                <hr />
                <div>

                <div class="form-group">
                    <label for="id_username" class="col-md-2 control-label">账号：</label>
                    <div class="col-md-10">
                        <input type="text" name="username" >
                    </div>
                </div>
                <div class="form-group">
                    <label for="id_password" class="col-md-2 control-label">密码：</label>
                    <div class="col-md-10">
                        <input type="password" name="password" >
                    </div>
                </div>
                <div class="form-group">
                    <div class="col-md-10">
                        <input type="submit" value="登录" class="btn btn-primary btn-block" />
                    </div>
                </div>
                 <br> <br><br><br><br><br>
                <div class="form-group">
                    <div class="col-md-8"> </div>
                    <div class="col-md-4">
                        没有账号？
                     <a href="/register" title="" class="btn btn-primary">立即注册</a>
                    </div>
                </div>

                </div>
            </form>
        </section>
    </div>
    <div class="col-md-4">
    </div>
</div>
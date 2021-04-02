# 该类的实例将会成为我们的 WSGI 应用
from flask import Flask
from markupsafe import escape
from flask import request
"""
接着我们创建一个该类的实例。
第一个参数是应用模块或者包的名称。
如果你使用一个单一模块，那么应当使用 __name__ ，因为名称会根据这个模块是按应用方式使用还是作为一个模块导入而发生变化
（可能是 '__main__' ，也可能是实际导入的名称）。
这个参数是必需的，这样 Flask 才能知道在哪里可以找到模板和静态文件等东西。更多内容详见 Flask 文档。
"""
app = Flask(__name__)


# 使用 route() 装饰器来告诉 Flask 触发函数的 URL 。
# 函数名称被用于生成相关联的 URL 。函数最后返回需要在用户浏览器中显示的信息。
@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return "do_the_login()"
	else:
		return "show_the_login_form()"

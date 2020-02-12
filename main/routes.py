import os , uuid
from datetime import datetime
from main import app , bcrypt , db
from flask import render_template , url_for , redirect , request , send_from_directory
from main.forms import Login , PostForm
from main.models import User , Post
from flask_login import login_user , logout_user , current_user , login_required
from flask_ckeditor import CKEditorField , upload_fail, upload_success

@app.route("/")
def index():
    posts = Post.query.all()
    return render_template('index.html' , posts = posts)

@app.route("/about")
def about():
    return render_template('about.html')
    

@app.route("/post/<int:post_id>/<string:slug>") 
def get_post(post_id , slug):
    post = Post.query.filter_by(id = post_id).first()

    if post:
        return render_template('post.html' , post = post)
    else:
        return render_template('error.html' , error = 'Page is not found')

@app.route("/login" , methods = ['GET' , 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        next_page = request.args.get('next')
        if user and bcrypt.check_password_hash(user.password , form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('index'))
    return render_template('login.html' , form = form)


@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('login'))
    else:
        return redirect(url_for('index'))
    

#--------- REQUIRE LOGIN -----------

@app.route("/add_post" , methods = ['GET' , 'POST']) 
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data , content = form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
        
    return render_template('add_post.html' , form = form)

@app.route("/update_about")
def update_about():
    #gerekli veritabanı işlemleri yapılır döndürülecek
    #redirect about yapması gerek
    return render_template('index.html')



@app.route("/update_post/<int:post_id>" , methods  = ['POST' , 'GET'])
@login_required
def update_post(post_id):
    form = PostForm()
    if request.method  == 'GET':
        post = Post.query.get(post_id)
        form.title.data= post.title
        form.content.data = post.content
        
        return render_template('update.html' , form = form)

    elif request.method  == 'POST' and form.validate_on_submit():
        post = Post.query.get(post_id)
        post.title = form.title.data 
        post.content = form.content.data
        db.session.commit()
        return redirect(url_for('index'))

@app.route("/delete/<int:post_id>" )
@login_required
def delete_post(post_id):

    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    print(post)
    return redirect(url_for('index'))

#--------- CKEDITOR UPLOAD -----------

@app.route('/files/<filename>')
@login_required
def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)

@app.route('/upload', methods=['POST'])
@login_required
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[1].lower()

    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')

    unique_filename = str(uuid.uuid4()) + "." + extension
    f.save(os.path.join(app.config['UPLOADED_PATH'], unique_filename))
    url = url_for('uploaded_files', filename=unique_filename)
    return upload_success(url=url)




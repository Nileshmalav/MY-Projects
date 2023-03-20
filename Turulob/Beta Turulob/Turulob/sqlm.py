from email.policy import default
from basicm import *


class userpassdb(UserMixin, db.Model):
    __tablename__ = 'userPassword'
    
    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    date_created = db.Column(db.DateTime, default=datetime.now)

    def get_id(self):
        return self.sno
    

class otpdb(db.Model):
    __tablename__ = 'OTP'

    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), default="None")
    email = db.Column(db.String(50), default="None")
    otp = db.Column(db.String(10), nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)


class userInfodb(db.Model):
    __tablename__ = 'userInfo'
    
    pic = open("defaultprofile.jpg", 'rb')
    filename = secure_filename("defaultprofile.jpg")
    mimetype = "image/jpeg"


    sno = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20))

    intro = db.Column(db.String(200), default="")

    gender = db.Column(db.String(100) )
    age = db.Column(db.String(5))

    location_City = db.Column(db.String(50))
    location_State = db.Column(db.String(50))
    location_Country = db.Column(db.String(50))

    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))
    
    distance = db.Column(db.String(100))
    
    facebook = db.Column(db.String(200), default="https://www.facebook.com/")
    instagram = db.Column(db.String(200), default="https://www.instagram.com/")

    img = db.Column(db.Text, default=pic.read())
    img_name = db.Column(db.Text, default=filename)
    img_mimetype = db.Column(db.Text, default=mimetype)

    membership = db.Column(db.String(50), default="Free")
    
    
    message_count = db.Column(db.Integer,default=0)
    notification_count = db.Column(db.Integer,default=0)

    date_created = db.Column(db.DateTime, default=datetime.now)
    
    
    
    
    posts = relationship("postsdb")
    other_profile_Images = relationship("otherProfileImagesdb")
    notification = relationship("notificationdb")
    save = relationship("savedb")
    shedule_Dates = relationship("sheduleDatesdb")
    like = relationship("likedb")
    superLike = relationship("superLikedb")

    def __repr__(self) -> str:
        return f"{self.sno} - {self.username} - {self.email} - {self.first_name} {self.last_name} "


class otherProfileImagesdb(db.Model):
    __tablename__ = 'otherProfileImages'
    
    id = db.Column(db.Integer, primary_key=True)
    
    username = db.Column(db.String, ForeignKey('userInfo.username'))
    
    img = db.Column(db.Text)
    name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.now)


class chatsdb(db.Model):
    __tablename__ = 'chats'
    
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")

    id = db.Column(db.Integer, primary_key=True)
    
    from_user = db.Column(db.String(50), nullable=False)
    to_user = db.Column(db.String(50), nullable=False)
    chat_message = db.Column(db.String(1000))

    chat_img = db.Column(db.Text)
    image_name = db.Column(db.Text)
    image_mimetype = db.Column(db.Text)
    
    delete_chat_to = db.Column(db.String(50))
    delete_chat_from = db.Column(db.String(50))

    alt_img_link = db.Column(db.Text)

    read = db.Column(db.String(50), default=False)
    
    chat_time = db.Column(db.String(50), default=time)
    date_created = db.Column(db.DateTime, default=datetime.now)


class chatsuserdb(db.Model):
    __tablename__ = 'chatUserInfo'
    
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")

    id = db.Column(db.Integer, primary_key=True)
    from_user = db.Column(db.String(50), nullable=False)
    to_user = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50))

    message_count_to = db.Column(db.Integer, default=0)
    message_count_from = db.Column(db.Integer, default=0)
    
    delete_chat_to = db.Column(db.String(50))
    delete_chat_from = db.Column(db.String(50))
    
    last_message = db.Column(db.String(1000))
    
    chat_user_time = db.Column(db.String(50), default=time)
    date_created = db.Column(db.DateTime, default=datetime.now)


class stickersdb(db.Model):
    __tablename__ = 'stickers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)
    alt_img = db.Column(db.Text)
    mimetype = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)


class superLikedb(db.Model):
    __tablename__ = 'superLike'
    
    id = db.Column(db.Integer, primary_key=True)
    from_user = db.Column(db.String(40), ForeignKey('userInfo.username'))
    to_user = db.Column(db.String(40))
    date_created = db.Column(db.DateTime, default=datetime.now)


class likedb(db.Model):
    __tablename__ = 'likes'
    
    id = db.Column(db.Integer, primary_key=True)
    from_user = db.Column(db.String(40), ForeignKey('userInfo.username'))
    to_user = db.Column(db.String(40))
    date_created = db.Column(db.DateTime, default=datetime.now)


class savedb(db.Model):
    __tablename__ = 'save'
    
    id = db.Column(db.Integer, primary_key=True)
    from_user = db.Column(db.String(40), ForeignKey('userInfo.username'))
    to_user = db.Column(db.String(40))
    name = db.Column(db.String(40))
    
    date_created = db.Column(db.DateTime, default=datetime.now)


class sheduleDatesdb(db.Model):
    __tablename__ = 'sheduleDate'
    
    id = db.Column(db.Integer, primary_key=True)
    from_user = db.Column(db.String(40), ForeignKey('userInfo.username'))
    to_user = db.Column(db.String(40))
    name = db.Column(db.String(40))
    
    date_time = db.Column(db.String(50))
    date_date = db.Column(db.String(50))
    
    location = db.Column(db.String(100))
    
    latitude = db.Column(db.String(30))
    longitude = db.Column(db.String(30))
    
    date_created = db.Column(db.DateTime, default=datetime.now)


class notificationdb(db.Model):
    __tablename__ = 'notification'
    
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")

    id = db.Column(db.Integer, primary_key=True)
    
    
    username = db.Column(db.String(40), ForeignKey('userInfo.username'))
    
    text = db.Column(db.String(100))
    title = db.Column(db.String(100))
    type = db.Column(db.String(50))
    
    link = db.Column(db.String(100), default="#")
    
    ntime = db.Column(db.String(50), default=time)
    date_created = db.Column(db.DateTime, default=datetime.now)


class postsdb(db.Model):
    __tablename__ = 'posts'
    
    __tablename__ = 'posts'
    time = datetime.now()
    time = time.strftime("%m/%d/%Y, %H:%M:%S")

    id = db.Column(db.Integer, primary_key=True)
    
    like_count = db.Column(db.Integer, default=0)
    comment = db.Column(db.Integer, default=0)
    
    username = db.Column(db.String(40), ForeignKey('userInfo.username'))
    name = db.Column(db.String(40))
    
    text = db.Column(db.String(150),default="")
    
    img = db.Column(db.Text)
    image_name = db.Column(db.Text)
    image_mimetype = db.Column(db.Text)
    
    
    like = relationship("postslikedb")
    comments = relationship("postsCommentsdb")

    ntime = db.Column(db.String(50), default=time)
    date_created = db.Column(db.DateTime, default=datetime.now)


class postsCommentsdb(db.Model):
    __tablename__ = 'postComments'
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey('posts.id'))
    from_username = db.Column(db.String(40))
    
    text = db.Column(db.String(150))
    
    date_created = db.Column(db.DateTime, default=datetime.now)
    
    
class postslikedb(db.Model):
    __tablename__ = 'postLike'
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey('posts.id'))
    from_username = db.Column(db.String(40))
    date_created = db.Column(db.DateTime, default=datetime.now)




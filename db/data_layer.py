import json, requests
from sqlalchemy import or_, and_
from db.base import DbManager
from db.entities import User, Like, Show

db = DbManager()

def get_json(url):
    response = requests.get(url)
    return json.loads(response.text)

def search_database(query):
    print('*******{}'.format(query))
    query_url = 'http://api.tvmaze.com/search/shows?q={}'.format(query)
    list_of_results = get_json(query_url)
    show_list = []
    for result in list_of_results:
        show_dict = result['show']
        tvmaze_id = show_dict['id']
        show_name = show_dict['name']
        show_image_url = show_dict['image']['medium']
        new_show = create_show(tvmaze_id, show_name, show_image_url)
        show_list.append(new_show)
    return show_list

def create_show(tvmaze_id, show_name, show_image_url):
    show = Show()
    show.tvmaze_id = tvmaze_id
    show.showname = show_name
    show.show_image_url = show_image_url
    return db.save(show)

def create_user(email, username, password):
    user = User()
    user.username = username
    user.email = email
    user.password = password
    return db.save(user)

def get_user_by_email(user_email):
    return db.open().query(User).filter(User.email == user_email).one()

def search_for_shows(query):
    pass

def get_shows_from_api(query):
    pass

def get_shows_from_db(name):
    show = None
    try:
        exchange = db.open().query(Show).filter(Show.showname == name).one()
    except:
        show = Show()
        json_data = get_json(url)
        exchange.parse_dictionary(json_data)
        db.save(show)
    return show

def like_show(show_id):
    like = Like()
    like.user_id = user_id
    return dbsave(like)

def unlike_show(show_id):
    like = db.open().query(Like).filer(Show.id == show_id).one()
    return db.delete(like)

def get_likes(user_id):
    return db.open().query(Like).filter(Like.user_id == user_id).all()

# def get_all_quotes():
#     return db.open().query(Quote).order_by(Quote.created_at.desc()).filter().all()

# def search_by_user_or_email(query):
#     return db.open().query(User).filter(or_(User.username.like('%{}%'.format(query)), User.email.like('%{}%'.format(query)))).all()

# def create_quote(user_id, content):
#     quote = Quote()
#     quote.user_id = user_id
#     quote.content = content
#     return db.save(quote)

# def delete_quote(quote_id):
#     quote = db.open().query(Quote).filter(Quote.id == quote_id).one()
#     return db.delete(quote)




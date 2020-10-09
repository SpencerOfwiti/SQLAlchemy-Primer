# This is a Python script to run a number of actions on the database.
from sqlalchemy.orm import aliased
from models import User, Session, Address, BlogPost, Keyword, Base, engine


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    session = Session()
    # transient state
    ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
    # pending state
    session.add(ed_user)
    # auto flush
    our_user = session.query(User).filter_by(name='ed').first()
    print(our_user)
    print(ed_user is our_user)
    session.add_all([
        User(name='wendy', fullname='Wendy Williams', nickname='windy'),
        User(name='mary', fullname='Mary Contrary', nickname='mary'),
        User(name='fred', fullname='Fred Flintstone', nickname='freddy')
    ])
    ed_user.nickname = 'eddie'
    print(session.dirty)
    print(session.new)
    # persistent state
    session.commit()
    print(ed_user.id)
    # roll back
    ed_user.name = 'Edwardo'
    fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
    session.add(fake_user)
    session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
    session.rollback()
    print(ed_user.name)
    print(fake_user in session)
    # querying
    # user object
    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)
    # class entities or columns
    for name, fullname in session.query(User.name, User.fullname):
        print(name, fullname)
    # keyed tuples
    for row in session.query(User, User.name).all():
        print(row.User, row.name)
    # column element label
    for row in session.query(User.name.label('name_label')).all():
        print(row.name_label)
    # aliases
    user_alias = aliased(User, name='user_alias')
    for row in session.query(user_alias, user_alias.name).all():
        print(row.user_alias)
    # limits
    for u in session.query(User).order_by(User.id)[1:3]:
        print(u)
    # filtering
    for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
        print(name)
    for name, in session.query(User.name).filter(User.name=='Ed Jones'):
        print(name)
    # working with related objects
    jack = User(name='jack', fullname='Jack Bean', nickname='jacques')
    print(jack.addresses)
    jack.addresses = [Address(email_address='jack@google.com'), Address(email_address='j25@yahoo.com')]
    print(jack.addresses[1])
    print(jack.addresses[1].user)
    session.add(jack)
    session.commit()
    jack = session.query(User).filter_by(name='jack').one()
    print(jack.addresses)
    # querying with joins
    for u, a in session.query(User, Address).filter(User.id==Address.user_id).filter(Address.email_address=='jack@google.com').all():
        print(u)
        print(a)
    user_j = session.query(User).join(Address).filter(Address.email_address=='jack@google.com').all()
    print(user_j)
    # using aliases
    adalias1 = aliased(Address)
    adalias2 = aliased(Address)
    for username, email1, email2 in session.query(User.name, adalias1.email_address, adalias2.email_address).\
        join(User.addresses.of_type(adalias1)).join(User.addresses.of_type(adalias2)).\
        filter(adalias1.email_address=='jack@google.com').filter(adalias2.email_address=='j25@yahoo.com'):
        print(username, email1, email2)
    # delete
    session.delete(jack)
    q = session.query(User).filter_by(name='jack').count()
    print(q)
    addr = session.query(Address).filter(Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])).count()
    print(addr)
    # many to many relationship
    wendy = session.query(User).filter_by(name='wendy').one()
    post = BlogPost('Wendy\'s Blog Post', 'This is a test', wendy)
    session.add(post)
    post.keywords.append(Keyword('wendy'))
    post.keywords.append(Keyword('firstpost'))
    firstposts = session.query(BlogPost).filter(BlogPost.keywords.any(keyword='firstpost')).all()
    print(firstposts)
    wendypost = wendy.posts.filter(BlogPost.keywords.any(keyword='firstpost')).all()
    print(wendypost)
    session.commit()

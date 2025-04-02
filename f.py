global_init(input())


def main():
    db_sess = create_session()
    for user in db_sess.query(User).all():
        print(user.id)


if __name__ == '__main__':
    main()

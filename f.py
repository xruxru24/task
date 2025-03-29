global_init(input())


def main():
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == 'module_1', User.age <= 21):
        print(f'{user.id} {user.surname} {user.name})


if __name__ == '__main__':
    main()

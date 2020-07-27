import pygit2


class MyRemoteCallbacks(pygit2.RemoteCallbacks):
    def credentials(self, url, username_from_url, allowed_types):
        if allowed_types & pygit2.credentials.GIT_CREDENTIAL_USERNAME:
            return pygit2.Username("victor-kovalov@yandex.ru")
        elif allowed_types & pygit2.credentials.GIT_CREDENTIAL_SSH_KEY:
            return pygit2.Keypair("git", "id_rsa.pub", "id_rsa", "")
        else:
            return None


if __name__ == '__main__':
    print("Cloning pygit2 over ssh")
    pygit2.clone_repository("https://github.com/MaximTretjakov/malamute", "malamute", callbacks=MyRemoteCallbacks())

    print("Cloning pygit2 over ssh with the username in the URL")
    keypair = pygit2.Keypair("git", "id_rsa.pub", "id_rsa", "")
    callbacks = pygit2.RemoteCallbacks(credentials=keypair)
    pygit2.clone_repository("ssh://git@github.com/libgit2/pygit2", "pygit2.git", callbacks=callbacks)

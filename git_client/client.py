import pygit2
import logging

from core.config import config

logging.getLogger('malamute_global_logger')


class CustomRemoteCallbacks(pygit2.RemoteCallbacks):
    """
    Сторонняя библиотека pygit2, порт libgit2 c языка си.
    Позволяет работать с git.
    """
    def credentials(self, url, username_from_url, allowed_types):
        if allowed_types & pygit2.credentials.GIT_CREDENTIAL_USERNAME:
            return pygit2.Username(config.read_from_conf()['user_name'])
        elif allowed_types & pygit2.credentials.GIT_CREDENTIAL_SSH_KEY:
            return pygit2.Keypair("git", "id_rsa.pub", "id_rsa", "")
        else:
            return None


class FetchDataFromGit:
    @staticmethod
    def clone_https(repo_name, build_dir, callback):
        try:
            pygit2.clone_repository(repo_name, build_dir, callbacks=callback)
        except Exception as e:
            logging.debug(e)

    @staticmethod
    def clone_ssh(self, repo_name, build_dir):
        try:
            key_pair = pygit2.Keypair("git", "id_rsa.pub", "id_rsa", "")
            callbacks = pygit2.RemoteCallbacks(credentials=key_pair)
            pygit2.clone_repository(repo_name, build_dir, callbacks=callbacks)
        except Exception as e:
            logging.debug(e)


git_obj = FetchDataFromGit()

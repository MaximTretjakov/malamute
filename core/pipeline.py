from core.handlers import GitHandler, BuildHandler, DeployHandler


def executor(tasks_obj):
    # создаем обработчики
    git = GitHandler()
    build = BuildHandler()
    deploy = DeployHandler()

    # связываем обработчики в цепь
    git.set_next(build).set_next(deploy)

    # обработка задач
    result = git.handle(tasks_obj)
    if result:
        print(f" Handler response: {result}", end="")
    else:
        print(f"  {tasks_obj} was left untouched.", end="")


if __name__ == '__main__':
    # все это будет приходить с фронта
    t = {
        "targets": 'https://github.com/MaximTretjakov/questionnaire/archive/master.zip',
        "build_dir": r"C:\Users\KARMA\Desktop\Projects\build\questionnaire.zip",
        "chunk_size": 150,
        "zip_name": "questionnaire.zip",
        "build_script_path": r"C:\Users\KARMA\Desktop\Projects\build\questionnaire-master\build_project.bat",
        "cwd": r'C:\Users\KARMA\Desktop\Projects\build\questionnaire-master'
    }

    executor(t)

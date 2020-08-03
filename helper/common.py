import zipfile
import logging


logger = logging.getLogger('malamute_global_logger')

# когда будет фронт это будет приходить с фронта в одном объекте
unzipped_project_dir = r'C:\Users\KARMA\Desktop\Projects\build'


def unzip_project(zip_obj):
    try:
        zip_file = unzipped_project_dir + '\\' + zip_obj['zip_name']
        with zipfile.ZipFile(zip_file, 'r') as zip_f:
            zip_f.extractall(unzipped_project_dir)
    except Exception as e:
        logger.debug(e)

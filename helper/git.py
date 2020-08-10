import requests


def download_project(request_obj):
    with requests.Session() as session:
        resp = session.get(request_obj['targets'], stream=True)
        with open(request_obj['build_dir'], 'wb') as file:
            for chunk in resp.iter_content(chunk_size=request_obj['chunk_size']):
                file.write(chunk)

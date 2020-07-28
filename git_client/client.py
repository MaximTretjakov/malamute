import time
import asyncio
import aiohttp

from core.config import config


async def fetch(target, file_name, chunk_size=10):
    async with aiohttp.ClientSession() as session:
        async with session.get(target) as resp:
            with open(file_name, 'wb') as fd:
                while True:
                    chunk = await resp.content.read(chunk_size)
                    if not chunk:
                        break
                    fd.write(chunk)


async def main(conf):
    tasks = []
    targets = conf['targets']
    build_dir = conf['build_dir']
    file_ext = conf['file_extension']
    chunk_size_bytes = conf['chunk_size']
    if not targets or not build_dir or not file_ext:
        raise AssertionError('Field "targets" or "build_dir or file_ext" in malamute.json config is empty. Set it.')
    for url in targets:
        file_name = url.split('/')[-3]
        path_to_build_dir = build_dir + file_name + file_ext
        task = asyncio.create_task(fetch(url, path_to_build_dir, chunk_size_bytes))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    conf_obj = config.read_from_conf()
    start = time.time()
    asyncio.run(main(conf_obj), debug=True)
    end = time.time()
    print(f'Total time : {end - start:.2}')

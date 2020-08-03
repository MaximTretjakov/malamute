import asyncio
import aiohttp


class Git:
    @staticmethod
    async def fetch(target, file_name, chunk_size=10):
        async with aiohttp.ClientSession() as session:
            async with session.get(target) as resp:
                with open(file_name, 'wb') as fd:
                    while True:
                        chunk = await resp.content.read(chunk_size)
                        if not chunk:
                            break
                        fd.write(chunk)

    async def main(self, conf):
        tasks = []
        targets = conf['targets']
        build_dir = conf['build_dir']
        chunk_size_bytes = conf['chunk_size']
        if not targets or not build_dir:
            raise AssertionError('Field "targets" or "build_dir in malamute.json config is empty. Set it.')
        for item in range(len(targets)):
            task = asyncio.create_task(self.fetch(targets[item], build_dir[item], chunk_size_bytes))
            tasks.append(task)
        await asyncio.gather(*tasks)

    def download_project(self, conf):
        asyncio.run(self.main(conf), debug=True)


git = Git()

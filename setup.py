from setuptools import setup, find_packages
import fastentrypoints

import subprocess

def readme():
    cmd = ['pandoc',
            '--from=markdown',
            '--to=rst',
            'README.md']
    return subprocess.check_output(cmd).decode()

setup(
        name = "rpgtime",
        version = '0.1.0',
        author = "bweir",
        author_email = "brett@lamestation.com",
        description = "RPG Time!",
        long_description = readme(),
        license = "GPLv3",
        url = "https://github.com/bweir/rpgtime",
        keywords = "game rpg pygame epic adventure",
        entry_points = {
            'console_scripts': [
                'rpgtime = rpgtime.__main__:main',
                ]
            },
        packages=find_packages(),
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Topic :: Games/Entertainment",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            ]
        )

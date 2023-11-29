from setuptools import setup, find_namespace_packages

setup(
    name='bot_helper',
    version='1',
    description='Package for sorting files in a specific folder, adding data to '
                'address book, read/update/delete it, adding notes etc.',
    url='https://github.com/Natali2411/GoIT-CoreProject',
    author='Nataliia Tiutiunnyk',
    author_email='nat.tiutiunnyk@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['prompt_toolkit', 'tabulate', 'pydantic', 'transliterate'],
    entry_points={'console_scripts': ['bot-helper = bot_helper.bot:main']}
)
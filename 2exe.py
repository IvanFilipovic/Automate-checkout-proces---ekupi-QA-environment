from distutils.core import setup
import py2exe

# Change the path in the following line for webdriver
data_files = [('selenium/webdriver/crome', ['C:/Users/ivan.filipovic1/PycharmProjects/pythonProject/venv/Lib/site-packages/selenium/webdriver/chrome/webdriver.py'])]

setup(
    name='Narudžbe',
    version='1.0',
    description='Narudžbe botovske',
    author='author name',
    author_email='author email',
    url='',
    windows=[{'script': 'bot.py'}],   # the main py file
    data_files=data_files,
    options={
        'py2exe':
            {
                'skip_archive': True,
                'optimize': 2,
            }
    }
)

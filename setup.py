from setuptools import setup, find_packages
 
classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
      ]


readme = ''
with open('README.txt', encoding="utf-8") as f:
    readme = f.read()


setup(
  name='dbleupy',
  version='3.0.0',
  description='This package offers you a more user friendly and easier way to interact with the discord-botlist.eu HTTP api.',
  long_description=readme,
  long_description_content_type="text/markdown",
  #charset="UTF-8",
  url='https://github.com/dbleu/python-library', 
  author='Florent Tahiri',
  author_email='florent.tahiri@gski.de',
  license='MIT', 
  classifiers=classifiers,
  keywords='dbleupy api http', 
  packages=find_packages(),
  install_requires=[''],
  python_requires='>=3.4.0',
)

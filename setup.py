from os.path import abspath, dirname, join
from setuptools import setup
from adventurelib import __version__


ROOT = abspath(dirname(__file__))


with open(join(ROOT, "README.md")) as fd:
    README = fd.read()

setup(
    name='adventxtend',
    description='Extension for adventurelib/adstrangerlib,
    long_description=README,
    long_description_content_type="text/markdown",
    version=__version__,
    author='LEHAtupointow',
    author_email='pezleha@gmail.com',
    url='https://github.com/textoverse/adventxtend',,
    py_modules=['adventxtend'],
    extras_require={
        ':python_version < "3.3"': [
            'adventurelib',
        ],
    },
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Games/Entertainment',
    ]
)

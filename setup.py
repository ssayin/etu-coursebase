from setuptools import setup

setup(
    name='coursebase',
    version='0.0.1',
    author='Serdar Sayın',
    author_email='nefer.kha.ptah@gmail.com',
    description="CLI for TOBB ETU Coursebase",
    license="BSD",
    py_module=['coursebase'],
    install_requires=[
        'lxml',
        'beautifulsoup4',
        'requests',
        'pandas',
    ],
    entry_points='''
        [console_scripts]
        coursebase=coursebase:main
    ''',
)

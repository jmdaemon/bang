from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='tem',
    version='0.1.7',
    license='MIT',
    author='Joseph Diza',
    author_email='josephm.diza@gmail.com',
    description='General purpose templating program to quickly setup projects and files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jmdaemon/bang',
    project_urls={
        'Bug Tracker': 'https://github.com/jmdaemon/bang/issues',
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    py_modules=['tem', 'tem.tmpl'],
    install_requires=[
        'argparse',
        'jinja2',
        'wora',
    ],
    entry_points={
        'console_scripts': [
            'tem = tem.tem:main',
        ],
    },
    test_suite='tests',
)

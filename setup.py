from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='bang-jmd',
    version='0.1.5',
    license='MIT',
    author='Joseph Diza',
    author_email='josephm.diza@gmail.com',
    description='Templating program to quickly start off projects with a bang',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jmdaemon/bang',
    project_urls={
        'Bug Tracker': 'https://github.com/jmdaemon/bang/issues',
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    py_modules=['bang', 'bang.tmpl'],
    install_requires=[
        'argparse',
        'jinja2',
        'wora',
    ],
    entry_points={
        'console_scripts': [
            'bang = bang.bang:main',
        ],
    },
    test_suite='tests',
)

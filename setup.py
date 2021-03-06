import setuptools

setuptools.setup(
    name='smidge',
    version='0.0.4',
    description='Small python tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xloem/pysmidge',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    packages=[
        'smidge'
    ],
    python_requires='>=3.7'
)

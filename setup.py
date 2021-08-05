import setuptools

setuptools.setup(
    name='smidge',
    version='0.0.1',
    descrption='Small python tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xloem/pysmidge',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPL 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7'
)
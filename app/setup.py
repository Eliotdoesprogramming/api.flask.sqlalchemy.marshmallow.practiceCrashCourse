from setuptools import setup

setup(
    name='flask-api',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
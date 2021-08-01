from setuptools import setup

setup(
    name='Gamma',
    version='0.2',
    url='https://github.com/rik-cross/gamma',
    description='A simple ECS game engine for Python, built on Pygame, with an emphasis on ease of use.',
    keywords=['Python', 'Pygame', 'ECS', 'Game Engine'],
    author='Rik Cross',
    author_email='rik@rikcross.net',
    license='MIT License',
    packages=['gamma'],
    install_requires=['pygame']
)
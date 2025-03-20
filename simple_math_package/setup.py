from setuptools import setup, find_packages

setup(
    name='simple_math_package',
    version='0.1.0',
    packages=find_packages(),
    description='A simple demonstration Python package for incrementing numbers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/simple_math_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)

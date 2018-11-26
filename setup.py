from setuptools import setup

setup(
    name='django-admitad',
    version='1.0.2',
    packages=['admitad'],
    install_requires=[
        'Django>=2.0',
    ],
    url='https://github.com/k0t3n/django-admitad',
    license='MIT License',
    author='k0t3n',
    author_email='k0t3n.mail@gmail.com',
    description='Django application that integrates Admitad CPA using postback requests',
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)

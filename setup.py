from setuptools import setup

setup(
    name='django-admitad',
    version='1.1.2',
    packages=['admitad'],
    package_data={
        'admitad': ['migrations/*.py']
    },
    install_requires=[
        'Django>=1.11',
    ],
    url='https://github.com/Picasel/django-admitad',
    license='MIT License',
    author='k0t3n',
    author_email='k0t3n.mail@gmail.com',
    description='Django application that integrates Admitad CPA using postback requests',
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)

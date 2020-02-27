from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='jflask',
    author='Djefry H. Hentris',
    author_email='djefry.h@gmail.com',
    url='https://github.com/djefry/jflask',
    description='Basic Event Messaging with Flask, Celery, SQLAlchemy and Postgres run in Docker',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='GPL',
    version='3',
    packages=['app'],
    install_requires=[
        'celery>=4.4.0',
        'Flask>=1.1.1',
        'Flask-Mail>==0.9.1',
        'Flask-SQLAlchemy>=2.4.1',
        'Flask-WTF>=0.14.3',
        'psycopg2>=2.8.4',
        'pytest>=5.3.5',
        'pytest-flask>=0.15.1',
        'pytest-flask-sqlalchemy>=1.0.2',
        'pytest-html>=2.0.1',
        'pytest-metadata>=1.8.0',
        'pytest-mock>=2.0.0',
        'redis>=3.4.1',
        'selenium>=3.141.0',
        'SQLAlchemy>=1.3.13',
        'SQLAlchemy-Utils>=0.36.1'
    ],
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Framework :: Flask',
    ]
)

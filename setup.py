import setuptools

setuptools.setup(
    name='heartbeat',
    version='0.1.0',
    long_description='',
    author='David Bukcley',
    author_email='buckley.w.david@gmail.com',
    url='https://github.com/buckley-w-david/heartbeat',
    include_package_data=True,
    packages=[
        'heartbeat',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'eventlet==0.23.0',
        'Flask==1.0.2',
        'Flask-SocketIO==3.0.1',
        'greenlet==0.4.13',
        'gunicorn==19.8.1',
    ],
    extras_require={
        'development': [
            'mypy==0.610',
            'pylint==1.9.2',
            'pytest==3.6.2',
            'pytest-cov==2.5.1',
            'black==18.6b3',
        ],
    },
)

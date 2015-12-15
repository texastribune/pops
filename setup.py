from setuptools import setup


setup(
    name='pops',
    version='0.2.0tt8',
    author='Travis Swicegood',
    author_email='travis@domain51.com',
    url='https://github.com/tswicegood/pops',
    packages=['pops', 'pops.menu', 'pops.templatetags'],
    include_package_data=True,
    license='Apache License, Version 2.0',
    description="Bootstrap styling for Django's admin",
    long_description=open('README.rst').read(),
    install_requires=[
        'django-admin-tools>=0.4.1',
        'BeautifulSoup>=3.2.0',
        'django-appconf>=0.4.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
    ],
)

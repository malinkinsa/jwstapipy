from setuptools import setup, find_packages

setup(
    name='jwstapipy',
    version='0.0.1',
    author='Sergey Malinkin',
    author_email='malinkinsa@yandex.ru',
    url='https://github.com/malinkinsa/jwstapipy',
    download_url='https://github.com/malinkinsa/jwstapipy/archive/refs/tags/0.0.1.tar.gz',
    description='Simple async python library for access to data from jwstapi.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='jwstapi space telescope james webb',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    install_requires=[
        'asyncio',
        'httpx',
    ],
)

import re
from setuptools import setup, find_packages

version = "0.1.0a"
requirements = ["requests"]
long_description = "My minimal discord webhook impl"
setup(
    name='synchooks',
    description=long_description,
    author='justanotherbyte',
    version=version,
    license='MIT',
    url='https://github.com/justanotherbyte/synchooks',
    keywords=["discord", "webhook", "requests"],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
)

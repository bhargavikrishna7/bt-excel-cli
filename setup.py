from setuptools import setup, find_namespace_packages

setup(
    name='bt-excel-cli',
    description='CLI for CRUD operations on spreadsheet',
    author="Bhargavi Bharatula",
    author_email="bhargavi.krishna7@gmail.com",
    version='0.0.1',
    py_modules=['bt-excel-cli'],
    packages_dir={'':'bt-excel-cli'},
    install_requires=['click', 
        'pandas'
    ],
    packages=find_namespace_packages(where='bt-excel-cli'),
    include_package_data=True,
    platforms=["Mac", "Linux"],
    entry_points={
        'console_scripts': [
            'bt-excel-cli=main:main',
        ]
    }
)

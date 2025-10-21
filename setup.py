from setuptools import setup, find_packages

setup(
    name='julie_package',  # Package name
    version='0.1',  # Version number
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=["pandas"],  # Package dependencies here
    author='Julie Vandenberghe',  
    author_email='julie.vandenberghe@lacatholille.fr',  
    description='filter and drop columns functionalities on csv files',
    long_description=open('README.md').read(),  # Reads the content of README.md
    long_description_content_type='text/markdown',  # Ensures correct rendering of Markdown
    url='https://github.com/julie-vandenberghe/csv-tools-julie.git',  # Project's URL (optional)
    classifiers=[
        'Programming Language :: Python :: 3',  # Specify supported Python versions
        'License :: OSI Approved :: MIT License',  # Specify the license (you can choose different one)
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)

from setuptools import setup, find_packages

setup(
    name='LibreNMSAPIClient',
    version='1.0',
    description='Python client for the LibreNMS API',
    url='https://github.com/electrocret/LibreNMSAPIClient',
    author='electrocret',
    author_email='email@example.com', 
    license='GPL-3.0',
    
    packages=find_packages(),
    
    install_requires=['requests>=2.28.1'],

    python_requires='>=3.6',
)
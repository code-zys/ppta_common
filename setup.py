from setuptools import setup, find_packages

setup(
    name='ppta_common',
    version='0.4.6',
    packages=find_packages(),
    install_requires=[
        'mongoengine',
        'tzlocal',
        'pytz',
        # 'boto3',
        'boto3-stubs[s3,sqs,textract,kms]',
        'blinker',
        'pydantic',
        'pydantic-settings',
        'python-jose',
        'imap_tools',
        'requests',
        'iso4217',
        'iso4217parse'
    ],
    description='Prepa Compta common module',
    author='Peter',
    url='https://github.com/code-zys/ppta_common',
)

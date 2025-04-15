from setuptools import setup, find_packages

setup(
    name='ppta_common',
    version='0.5.49',
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
    description='IYVO common module',
    author='Peter',
    url='https://github.com/code-zys/ppta_common',
)

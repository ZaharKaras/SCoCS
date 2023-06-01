from setuptools import setup

setup(
    name='zahar-custom-serializer',
    version='0.2.3',
    packages=[
        "03-LAB.source.serializers"
    ],
    entry_points={
        'console_scripts': [
            "custom-serialize = 03-LAB.source.serializers"
        ]
    },
    license='MIT',
    author='zahar',
    author_email='zahar.karas@gmail.com',
    description='Python JSON and XML serializer',
)
from setuptools import find_packages, setup

with open('README') as f:
    readme_text = f.read()

with open('LICENSE') as f:
    license_text = f.read()

setup(
    name='pyinputevent',
    version='0.1',
    long_description=readme_text,
    url='http://github.com/ammgws/pyinputevent',
    packages=find_packages(exclude=('tests', 'docs')),
    license=license_text,
    zip_safe=False,
    install_requires=[
    ],
)

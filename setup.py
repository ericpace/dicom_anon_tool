"""dicom_anonymiser setup"""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Eric Pace",
    author_email="ericpace@pm.me",
    name='dicom_anonymiser',
    license="GNU GPLv3",
    description='dicom_anonymiser anonymised dicom files in bulk with user customisable tags.',
    version='v0.1',
    long_description=README,
    url='https://github.com/ericpace/dicom_anon_tool',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=[
        'gooey',
        'pydicom'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
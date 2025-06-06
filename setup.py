from setuptools import setup, find_packages

setup(
    name="temporizador",
    version="0.1",
    packages=find_packages(),       
    install_requires=[],
        entry_points={
        'console_scripts': [
            'temporizador=temporizador.__main__:main',
        ]
    },
    author="Eduardo Sánchez",
    author_email="eduardosanchezterroba@gmail.com",
    description="Paquete de cronómetro y cuenta atrás",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/edusanchez11/temporizador",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 
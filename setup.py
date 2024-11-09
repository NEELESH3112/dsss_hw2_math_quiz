from setuptools import setup, find_packages

setup(
    name="math_quiz",  
    version="0.1",  
    packages=find_packages(),  
    install_requires=[  
        'unittest',  
    ],
    entry_points={  # Optional, if you want to make command-line tools
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',  
        ],
    },
    classifiers=[  
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author="Neelesh Babu",  
    author_email="nneelesh31.12@gmail.com",  
    description="A simple math quiz game",  
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",  
)


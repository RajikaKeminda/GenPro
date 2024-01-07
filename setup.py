from setuptools import setup, find_packages

setup(
    name='genpro',
    version='0.1.2',
    author="Rajika Keminda",
    author_email="rkeminda0@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click', 'python-dotenv', 'rich', 'openai'
    ],
    keywords=["cli", "AI", "python", "project manager"],
    entry_points={
        'console_scripts': [
            'gp = genpro.commands:cli',
            'gen = genpro.commands:cli'
        ],
    },
)
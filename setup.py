from setuptools import setup, find_packages
import platform

system = platform.system()
cpu = platform.processor()

def read_requirements():
    if system == 'Darwin':
        requirement_file = 'requirements.txt'
        if cpu == 'arm':
            print("Macbook with arm cpu might not work well...")
    elif system == 'Linux':
        requirement_file = 'requirements_linux.txt'
    else:
        requirement_file = 'requirements_win.txt'
    with open(requirement_file) as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

setup(
    name='college894model',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    python_requires='>=3.7.4'
)

from setuptools import setup

setup(name='gameoflife',
      version='0.1',
      description='Game of Life',
      url='https://github.com/jankrepl/gameoflife',
      author='Jan',
      license='MIT',
      packages=['gameoflife'],
      entry_points={'console_scripts': ['gol = gameoflife.cli']},
      install_requires=['numpy==1.15.4', 'pygame==1.9.4'],
      )
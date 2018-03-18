from setuptools import setup
import sys

if sys.version_info.major != 3:
    print('This package is only compatible with Python 3, but you are running '
          'Python {}. The installation will likely fail.'.format(sys.version_info.major))

setup(name='gym_vecenv',
      version='1.0',
      description='Python3 wrapper for running multiple OpenAI Gym compatible environments in parallel',
      url='https://github.com/agakshat/gym_vecenv',
      author='Akshat Agarwal',
      author_email='agarwalaks30@gmail.com',
      license='MIT',
      packages=['gym_vecenv'],
      install_requires=['cloudpickle','gym','numpy'],
      zip_safe=False)
from setuptools import setup

setup(name='api-ui',
      version='0.1',
      description='UI application for rentals API',
      url='https://github.com/Leandrojaviercepeda/tp2-nsql',
      author='Cepeda Leandro',
      author_email='leandrojaviercepeda@gmail.com',
      license='MIT',
      packages=['requests, flask'],
      install_requires=[
          'requests, flask',
      ],
      zip_safe=False)
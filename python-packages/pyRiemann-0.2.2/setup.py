from setuptools import setup,find_packages

setup(name='pyriemann',
      version='0.2.1',
      description='Riemannian Geometry for python',
      url='',
      author='Alexandre Barachant',
      author_email='alexandre.barachant@gmail.com',
      license='BSD (3-clause)',
      packages=find_packages(),
      install_requires=['numpy','scipy','scikit-learn'],
      zip_safe=False)
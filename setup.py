from setuptools import setup

setup(name='keras_lr_finder',
      version='0.1',
      description='Learning rate finder for Keras.',
      url='http://github.com/surmenok/keras_lr_finder',
      author='Pavel Surmenok',
      author_email='pavel@surmenok.com',
      license='MIT',
      packages=['keras_lr_finder'],
      install_requires=[
            'keras>=2.0.0',
            'matplotlib'
      ],
      zip_safe=False)
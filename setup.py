from setuptools import find_packages, setup


VERSION = '0.1.0'
DESCRIPTION = ''
AUTHOR = 'hkakitani'
# AUTHOR_EMAIL = ''
# URL = ''
# LICENSE = 'Apache 2.0'
# KEYWORDS = ['']
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    # 'License :: OSI Approved :: Apache Software License',
    # 'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    # 'Programming Language :: Python :: 3.7',
    # 'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries',
]


setup(name='SincNet',
      version=VERSION,
      description=DESCRIPTION,
      long_description=open('SincNet/README.md', 'r').read(),
      long_description_content_type='text/markdown',
      author=AUTHOR,
    #   author_email=AUTHOR_EMAIL,
    #   url=URL,
    #   license=LICENSE,
    #   keywords=KEYWORDS,
      packages=find_packages(),
      install_requires=[
          'numpy',
        #  'torch>=1.5',
        #   'torchaudio>=0.5.0',
        #   'tqdm'
      ],
      classifiers=CLASSIFIERS,
)

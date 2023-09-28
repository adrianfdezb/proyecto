from setuptools import setup, find_packages


setup(
    name='proyecto',
    version='0.1',
    packages=find_packages(),
    install_requires=[streamlit,
                      scikit-learn==1.3.0,
                      pickleshare==0.7.5,
                      pandas,
                      numpy,
                      altair,
                      requests,
                      validators,
                      Pillow==8.4.0,
                      git+https://github.com/adrianfdezb/proyecto.git@main#egg=proyecto&subdirectory=app/utils
    ]
)

from setuptools import setup, find_packages


requirements = [
    'streamlit',
    'scikit-learn==1.3.0',
    'pickleshare==0.7.5',
    'pandas',
    'numpy',
    'altair',
    'requests',
    'validators',
    'Pillow==8.4.0',
    'Modelo_XGBoostRegresion'
]

setup(
    name='proyecto',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements
)

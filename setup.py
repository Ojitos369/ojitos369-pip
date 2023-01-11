from setuptools import setup
 
# download_url='https://github.com/RDCH106/parallel_foreach_submodule/archive/v0.1.tar.gz', # Te lo explico a continuación
setup(
    name='ojitos369',
    packages=['ojitos369'], # Mismo nombre que en la estructura de carpetas de arriba
    include_package_data=True,
    version='0.22',
    license='LGPL v3', # La licencia que tenga tu paquete
    description='Funciones de utilidades de ojitos369',
    long_description='Funciones de utilidades de ojitos369\nRevizar README en:\nhttps://github.com/Ojitos369/ojitos369-pip',
    author='Ojitos369',
    author_email='ojitos369@gmail.com',
    url='https://github.com/Ojitos369/ojitos369-pip', # Usa la URL del repositorio de GitHub
    keywords='Utilidades de ojitos369', # Palabras que definan tu paquete
    classifiers=[],
)
"""
# sudo pip install setuptools twine
py3 setup.py sdist
twine upload dist/*
"""
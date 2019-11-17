from setuptools import setup

setup(
    # nombre comando
    name = 'pv',
    version = '0.1',
    py_modules = ['pv'],
    # librería requerida
    install_requires = ['Click'],
    # Punto de entrada: le indicamos que es el método "cli" dentro de pv.py. entiendo que "pv" hace referencia al nombre
    # del comando indicado en "name"
    # Documentacion: https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point
    entry_points = '''
        [console_scripts]
        pv=pv:cli
    '''
)
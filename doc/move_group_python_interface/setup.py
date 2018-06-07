from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['package_dir'] = {'': 'src'}
d['packages'] = ['move_group_python_interface']

setup(**d)

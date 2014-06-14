from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

import numpy


a = Extension("agent", ["core/agent.pyx"],
    include_dirs = [numpy.get_include()])
b = Extension("block", ["core/block.pyx"],
    include_dirs = [numpy.get_include()])
c = Extension("cog", ["core/cog.pyx"],
    include_dirs = [numpy.get_include()])
d = Extension("daisychain", ["core/daisychain.pyx"],
    include_dirs = [numpy.get_include()])
e = Extension("hub", ["core/hub.pyx"],
    include_dirs = [numpy.get_include()])
f = Extension("tools", ["core/tools.pyx"],
    include_dirs = [numpy.get_include()])
g = Extension("ziptie", ["core/ziptie.pyx"],
    include_dirs = [numpy.get_include()])

                
setup(ext_modules=[a,b,c,d,e,f,g],
      cmdclass = {'build_ext': build_ext})

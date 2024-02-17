project('PkgName', 'c')
add_global_arguments(language : 'c')

py = import('python').find_installation()

# installs the package, which only contains the ctypes wrapper
py.install_sources(
  [
    'pkgname/__init__.py',
    'pkgname/wrapper.py',
  ],
  subdir: 'pkgname'
)

# compiles the shared library and puts it in the package installation folder
incdir = include_directories('pkgname/c/include')
sources = ['pkgname/c/mylib.c']
shared_library('sharedlibname',
    sources,
    include_directories : incdir,
    install: true,
    install_dir: py.get_install_dir() / 'pkgname/.sharedlibs'
)

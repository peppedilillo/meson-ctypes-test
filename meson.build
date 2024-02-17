project('TestPackage', 'c')
add_global_arguments('-D NDEBUG', language : 'c')

py = import('python').find_installation()

py.install_sources(
  [
    'pkgname/__init__.py',
    'pkgname/wrapper.py',
  ],
  subdir: 'pkgname'
)

incdir = include_directories('pkgname/c/include')
sources = ['pkgname/c/mylib.c']
shared_library('sharedlibname',
    sources,
    include_directories : incdir,
    install: true,
    install_dir: py.get_install_dir() / 'pkgname/.sharedlibs'
)

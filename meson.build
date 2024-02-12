project('mylib', 'c')
add_global_arguments('-D NDEBUG', language : 'c')

py = import('python').find_installation(pure: false)

py.install_sources(
    ['mypkg/wrapper.py'],
    subdir: 'mypkg'
)
message(py.get_install_dir())

incdir = include_directories('source/include')
sources = ['source/mylib.c']
shared_library('mylib',
    sources,
    include_directories : incdir,
    install: true,
    install_dir: py.get_install_dir() / 'mypkg'
)
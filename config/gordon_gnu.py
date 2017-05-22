import os

is_arch_valid = 1

#python_lt_27 = 1

flags_arch = '-O3 -Wall -g'
flags_link  = '-rdynamic'

cc   = 'gcc'
f90  = 'gfortran'

flags_prec_single = '-fdefault-real-4 -fdefault-double-8'
flags_prec_double = '-fdefault-real-8 -fdefault-double-8'


libpath_fortran = ''
libs_fortran    = ['gfortran']

home = '/Users/Thomas/Documents/College/16-17 Internship'

hdf5_path = '/usr/local/Cellar/hdf5/1.10.0-patch1/'
hdf5_inc = hdf5_path + '/include'
hdf5_lib = hdf5_path + '/lib'
mpi_path     = os.environ['MPIHOME']
#charm_path   = home + '/public/Charm/651/gnu/mvapich2/charm'
charm_path   = home + '/Charm/charm/'
papi_path    = home
#hdf5_path    = home + '/public'
#mpi_path     = home + '/public'
png_path     = '/usr/local/Cellar/libpng/1.6.29/'
grackle_path = home + '/public/Grackle/src/clib'

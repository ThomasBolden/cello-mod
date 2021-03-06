import os

is_arch_valid = 1

#python_lt_27 = 1

#flags_arch = '-g'
#flags_arch = '-Ofast' # ERROR: ipo linking
flags_arch = '-O3'
flags_link  = ''

cc   = 'icc'
f90  = 'ifort'

flags_prec_single = '-r4'
flags_prec_double = '-r8'

libpath_fortran = ''
libs_fortran    = ['imf','ifcore','ifport','stdc++','intlc']

home = os.environ['HOME']

libpath_fortran = ''
libs_fortran    = ['ifcore']

home = os.environ["HOME"]
charm_path = home + '/Charm/charm'
papi_path  = home
hdf5_path  = os.environ['HDF5HOME']
hdf5_inc = hdf5_path + '/include'
hdf5_lib = hdf5_path + '/lib'
mpi_path   = os.environ['MPIHOME']

png_path   = '/usr/lib64'
grackle_path = home + '/Grackle/src/clib'


#
# Enzo-P/Cello Configuration file for NCSA Blue Waters
#
# See README.ncsa_bw for additional information

import os

f90 = 'gfortran'
cxx = 'g++'
cc  = 'gcc'

python_lt_27 = 1

node_size = 32 # for BW integer cores

is_arch_valid = 1

flags_arch = '-O3'
flags_link  = '-static -ldl -lc'

flags_prec_single = ''
flags_prec_double = ''

cc   = 'gcc'
f90  = 'gfortran'

libpath_fortran = ''
libs_fortran    = ['gfortran']

home = '/u/sciteam/bolden'  #os.environ['HOME']

charm_path = home + '/Cello/charm'
png_path   = home + '/Cello/libpng'
hdf5_path  = '/opt/cray/hdf5/1.8.16'  #os.environ["HDF5_DIR"]
hdf5_inc = hdf5_path + '/include'
hdf5_lib = hdf5_path + '/lib'
grackle_path = home + '/local'

if (type == "mpi"):
   parallel_run = "aprun -n 8"

# --------------------------------------------------------------------------- #
#
# Enzo-P/Cello Configuration file for NCSA Blue Waters
#
# See README.ncsa_bw for additional information
'''
import os

f90 = {}
cxx = {}
cc  = {}

python_lt_27 = 1

node_size = 32 # for BW integer cores

is_arch_valid = 1

flags_arch = '-O3 -std=gnu++11'
flags_link  = '-std=gnu++11'

flags_prec_single = ''
flags_prec_double = ''

cc   = 'cc'
f90  = 'ftn'

libpath_fortran = ''
libs_fortran    = ['gfortran']

home = os.environ['HOME']

charm_path = home + '/Charm/charm'
png_path   = ''
hdf5_path  = os.environ["HDF5_DIR"]
hdf5_inc = hdf5_path + '/include'
hdf5_lib = hdf5_path + '/lib'

if (type == "mpi"):
   parallel_run = "aprun -n 8"
'''
import builtins as _mod_builtins
import collections as _mod_collections

class CompoundType(_mod_builtins.object):
    '\nA `netCDF4.CompoundType` instance is used to describe a compound data\ntype, and can be passed to the the `netCDF4.Dataset.createVariable` method of\na `netCDF4.Dataset` or `netCDF4.Group` instance. \nCompound data types map to numpy structured arrays.\nSee `netCDF4.CompoundType.__init__` for more details.\n\nThe instance variables `dtype` and `name` should not be modified by\nthe user.\n    '
    __class__ = CompoundType
    def __init__(self):
        '\n        ***`__init__(group, datatype, datatype_name)`***\n\n        CompoundType constructor.\n\n        **`group`**: `netCDF4.Group` instance to associate with the compound datatype.\n\n        **`datatype`**: A numpy dtype object describing a structured (a.k.a record)\n        array.  Can be composed of homogeneous numeric or character data types, or\n        other structured array data types.\n\n        **`datatype_name`**: a Python string containing a description of the\n        compound data type.\n\n        ***Note 1***: When creating nested compound data types,\n        the inner compound data types must already be associated with CompoundType\n        instances (so create CompoundType instances for the innermost structures\n        first).\n\n        ***Note 2***: `netCDF4.CompoundType` instances should be created using the\n        `netCDF4.Dataset.createCompoundType`\n        method of a `netCDF4.Dataset` or `netCDF4.Group` instance, not using this class directly.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __unicode__(self):
        pass
    
    @property
    def _nc_type(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    @property
    def dtype_view(self):
        pass
    
    @property
    def name(self):
        pass
    

class Dataset(_mod_builtins.object):
    "\nA netCDF `netCDF4.Dataset` is a collection of dimensions, groups, variables and\nattributes. Together they describe the meaning of data and relations among\ndata fields stored in a netCDF file. See `netCDF4.Dataset.__init__` for more\ndetails.\n\nA list of attribute names corresponding to global netCDF attributes\ndefined for the `netCDF4.Dataset` can be obtained with the\n`netCDF4.Dataset.ncattrs` method.\nThese attributes can be created by assigning to an attribute of the\n`netCDF4.Dataset` instance. A dictionary containing all the netCDF attribute\nname/value pairs is provided by the `__dict__` attribute of a\n`netCDF4.Dataset` instance.\n\nThe following class variables are read-only and should not be\nmodified by the user.\n\n**`dimensions`**: The `dimensions` dictionary maps the names of\ndimensions defined for the `netCDF4.Group` or `netCDF4.Dataset` to instances of the\n`netCDF4.Dimension` class.\n\n**`variables`**: The `variables` dictionary maps the names of variables\ndefined for this `netCDF4.Dataset` or `netCDF4.Group` to instances of the \n`netCDF4.Variable` class.\n\n**`groups`**: The groups dictionary maps the names of groups created for\nthis `netCDF4.Dataset` or `netCDF4.Group` to instances of the `netCDF4.Group` class (the\n`netCDF4.Dataset` class is simply a special case of the `netCDF4.Group` class which\ndescribes the root group in the netCDF4 file).\n\n**`cmptypes`**: The `cmptypes` dictionary maps the names of\ncompound types defined for the `netCDF4.Group` or `netCDF4.Dataset` to instances of the\n`netCDF4.CompoundType` class.\n\n**`vltypes`**: The `vltypes` dictionary maps the names of\nvariable-length types defined for the `netCDF4.Group` or `netCDF4.Dataset` to instances \nof the `netCDF4.VLType` class.\n\n**`enumtypes`**: The `enumtypes` dictionary maps the names of\nEnum types defined for the `netCDF4.Group` or `netCDF4.Dataset` to instances \nof the `netCDF4.EnumType` class.\n\n**`data_model`**: `data_model` describes the netCDF\ndata model version, one of `NETCDF3_CLASSIC`, `NETCDF4`,\n`NETCDF4_CLASSIC`, `NETCDF3_64BIT_OFFSET` or `NETCDF3_64BIT_DATA`.\n\n**`file_format`**: same as `data_model`, retained for backwards compatibility.\n\n**`disk_format`**: `disk_format` describes the underlying\nfile format, one of `NETCDF3`, `HDF5`, `HDF4`,\n`PNETCDF`, `DAP2`, `DAP4` or `UNDEFINED`. Only available if using\nnetcdf C library version >= 4.3.1, otherwise will always return\n`UNDEFINED`.\n\n**`parent`**: `parent` is a reference to the parent\n`netCDF4.Group` instance. `None` for the root group or `netCDF4.Dataset`\ninstance.\n\n**`path`**: `path` shows the location of the `netCDF4.Group` in\nthe `netCDF4.Dataset` in a unix directory format (the names of groups in the\nhierarchy separated by backslashes). A `netCDF4.Dataset` instance is the root\ngroup, so the path is simply `'/'`.\n\n**`keepweakref`**: If `True`, child Dimension and Variables objects only keep weak \nreferences to the parent Dataset or Group.\n    "
    __class__ = Dataset
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __enter__(self):
        return self
    
    def __exit__(self):
        pass
    
    def __getattr__(self):
        pass
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self):
        '\n        **`__init__(self, filename, mode="r", clobber=True, diskless=False,\n        persist=False, keepweakref=False, format=\'NETCDF4\')`**\n\n        `netCDF4.Dataset` constructor.\n\n        **`filename`**: Name of netCDF file to hold dataset. Can also\n\tbe a python 3 pathlib instance or the URL of an OpenDAP dataset.  When memory is\n\tset this is just used to set the `filepath()`.\n        \n        **`mode`**: access mode. `r` means read-only; no data can be\n        modified. `w` means write; a new file is created, an existing file with\n        the same name is deleted. `a` and `r+` mean append (in analogy with\n        serial files); an existing file is opened for reading and writing.\n        Appending `s` to modes `w`, `r+` or `a` will enable unbuffered shared\n        access to `NETCDF3_CLASSIC`, `NETCDF3_64BIT_OFFSET` or\n        `NETCDF3_64BIT_DATA` formatted files.\n        Unbuffered access may be useful even if you don\'t need shared\n        access, since it may be faster for programs that don\'t access data\n        sequentially. This option is ignored for `NETCDF4` and `NETCDF4_CLASSIC`\n        formatted files.\n        \n        **`clobber`**: if `True` (default), opening a file with `mode=\'w\'`\n        will clobber an existing file with the same name.  if `False`, an\n        exception will be raised if a file with the same name already exists.\n        \n        **`format`**: underlying file format (one of `\'NETCDF4\',\n        \'NETCDF4_CLASSIC\', \'NETCDF3_CLASSIC\'`, `\'NETCDF3_64BIT_OFFSET\'` or\n        `\'NETCDF3_64BIT_DATA\'`.\n        Only relevant if `mode = \'w\'` (if `mode = \'r\',\'a\'` or `\'r+\'` the file format\n        is automatically detected). Default `\'NETCDF4\'`, which means the data is\n        stored in an HDF5 file, using netCDF 4 API features.  Setting\n        `format=\'NETCDF4_CLASSIC\'` will create an HDF5 file, using only netCDF 3\n        compatible API features. netCDF 3 clients must be recompiled and linked\n        against the netCDF 4 library to read files in `NETCDF4_CLASSIC` format.\n        `\'NETCDF3_CLASSIC\'` is the classic netCDF 3 file format that does not\n        handle 2+ Gb files. `\'NETCDF3_64BIT_OFFSET\'` is the 64-bit offset\n        version of the netCDF 3 file format, which fully supports 2+ GB files, but\n        is only compatible with clients linked against netCDF version 3.6.0 or\n        later. `\'NETCDF3_64BIT_DATA\'` is the 64-bit data version of the netCDF 3\n        file format, which supports 64-bit dimension sizes plus unsigned and\n        64 bit integer data types, but is only compatible with clients linked against\n        netCDF version 4.4.0 or later.\n        \n        **`diskless`**: If `True`, create diskless (in memory) file.  \n        This is an experimental feature added to the C library after the\n        netcdf-4.2 release.\n        \n        **`persist`**: if `diskless=True`, persist file to disk when closed\n        (default `False`).\n\n        **`keepweakref`**: if `True`, child Dimension and Variable instances will keep weak\n        references to the parent Dataset or Group object.  Default is `False`, which\n        means strong references will be kept.  Having Dimension and Variable instances\n        keep a strong reference to the parent Dataset instance, which in turn keeps a\n        reference to child Dimension and Variable instances, creates circular references.\n        Circular references complicate garbage collection, which may mean increased\n        memory usage for programs that create may Dataset instances with lots of\n        Variables. It also will result in the Dataset object never being deleted, which\n        means it may keep open files alive as well. Setting `keepweakref=True` allows\n        Dataset instances to be garbage collected as soon as they go out of scope, potentially\n        reducing memory usage and open file handles.  However, in many cases this is not\n        desirable, since the associated Variable instances may still be needed, but are\n        rendered unusable when the parent Dataset instance is garbage collected.\n        \n        **`memory`**: if not `None`, open file with contents taken from this block of memory.\n        Must be a sequence of bytes.  Note this only works with "r" mode.\n\n        **`encoding`**: encoding used to encode filename string into bytes.\n        Default is None (`sys.getdefaultfileencoding()` is used).\n\n        **`parallel`**: open for parallel access using MPI (requires mpi4py and\n        parallel-enabled netcdf-c and hdf5 libraries).  Default is `False`. If\n        `True`, `comm` and `info` kwargs may also be specified.\n\n        **`comm`**: MPI_Comm object for parallel access. Default `None`, which\n        means MPI_COMM_WORLD will be used.  Ignored if `parallel=False`.\n\n        **`info`**: MPI_Info object for parallel access. Default `None`, which\n        means MPI_INFO_NULL will be used.  Ignored if `parallel=False`.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @property
    def __orthogonal_indexing__(self):
        pass
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __unicode__(self):
        pass
    
    def _close(self):
        pass
    
    def _enddef(self):
        pass
    
    @property
    def _grpid(self):
        pass
    
    @property
    def _isopen(self):
        pass
    
    def _redef(self):
        pass
    
    def close(self):
        '\n**`close(self)`**\n\nClose the Dataset.\n        '
        pass
    
    @property
    def cmptypes(self):
        pass
    
    def createCompoundType(self):
        "\n**`createCompoundType(self, datatype, datatype_name)`**\n\nCreates a new compound data type named `datatype_name` from the numpy\ndtype object `datatype`.\n\n***Note***: If the new compound data type contains other compound data types\n(i.e. it is a 'nested' compound type, where not all of the elements\nare homogeneous numeric data types), then the 'inner' compound types **must** be\ncreated first.\n\nThe return value is the `netCDF4.CompoundType` class instance describing the new\ndatatype."
        pass
    
    def createDimension(self):
        '\n**`createDimension(self, dimname, size=None)`**\n\nCreates a new dimension with the given `dimname` and `size`.\n\n`size` must be a positive integer or `None`, which stands for\n"unlimited" (default is `None`). Specifying a size of 0 also\nresults in an unlimited dimension. The return value is the `netCDF4.Dimension`\nclass instance describing the new dimension.  To determine the current\nmaximum size of the dimension, use the `len` function on the `netCDF4.Dimension`\ninstance. To determine if a dimension is \'unlimited\', use the\n`netCDF4.Dimension.isunlimited` method of the `netCDF4.Dimension` instance.'
        pass
    
    def createEnumType(self):
        '\n**`createEnumType(self, datatype, datatype_name, enum_dict)`**\n\nCreates a new Enum data type named `datatype_name` from a numpy\ninteger dtype object `datatype`, and a python dictionary\ndefining the enum fields and values.\n\nThe return value is the `netCDF4.EnumType` class instance describing the new\ndatatype.'
        pass
    
    def createGroup(self):
        "\n**`createGroup(self, groupname)`**\n\nCreates a new `netCDF4.Group` with the given `groupname`.\n\nIf `groupname` is specified as a path, using forward slashes as in unix to\nseparate components, then intermediate groups will be created as necessary \n(analogous to `mkdir -p` in unix).  For example,\n`createGroup('/GroupA/GroupB/GroupC')` will create `GroupA`,\n`GroupA/GroupB`, and `GroupA/GroupB/GroupC`, if they don't already exist.\nIf the specified path describes a group that already exists, no error is\nraised.\n\nThe return value is a `netCDF4.Group` class instance."
        pass
    
    def createVLType(self):
        '\n**`createVLType(self, datatype, datatype_name)`**\n\nCreates a new VLEN data type named `datatype_name` from a numpy\ndtype object `datatype`.\n\nThe return value is the `netCDF4.VLType` class instance describing the new\ndatatype.'
        pass
    
    def createVariable(self):
        '\n**`createVariable(self, varname, datatype, dimensions=(), zlib=False,\ncomplevel=4, shuffle=True, fletcher32=False, contiguous=False, chunksizes=None,\nendian=\'native\', least_significant_digit=None, fill_value=None)`**\n\nCreates a new variable with the given `varname`, `datatype`, and\n`dimensions`. If dimensions are not given, the variable is assumed to be\na scalar.\n\nIf `varname` is specified as a path, using forward slashes as in unix to\nseparate components, then intermediate groups will be created as necessary \nFor example, `createVariable(\'/GroupA/GroupB/VarC\', float, (\'x\',\'y\'))` will create groups `GroupA`\nand `GroupA/GroupB`, plus the variable `GroupA/GroupB/VarC`, if the preceding\ngroups don\'t already exist.\n\nThe `datatype` can be a numpy datatype object, or a string that describes\na numpy dtype object (like the `dtype.str` attribute of a numpy array).\nSupported specifiers include: `\'S1\' or \'c\' (NC_CHAR), \'i1\' or \'b\' or \'B\'\n(NC_BYTE), \'u1\' (NC_UBYTE), \'i2\' or \'h\' or \'s\' (NC_SHORT), \'u2\'\n(NC_USHORT), \'i4\' or \'i\' or \'l\' (NC_INT), \'u4\' (NC_UINT), \'i8\' (NC_INT64),\n\'u8\' (NC_UINT64), \'f4\' or \'f\' (NC_FLOAT), \'f8\' or \'d\' (NC_DOUBLE)`.\n`datatype` can also be a `netCDF4.CompoundType` instance\n(for a structured, or compound array), a `netCDF4.VLType` instance\n(for a variable-length array), or the python `str` builtin\n(for a variable-length string array). Numpy string and unicode datatypes with\nlength greater than one are aliases for `str`.\n\nData from netCDF variables is presented to python as numpy arrays with\nthe corresponding data type.\n\n`dimensions` must be a tuple containing dimension names (strings) that\nhave been defined previously using `netCDF4.Dataset.createDimension`. The default value\nis an empty tuple, which means the variable is a scalar.\n\nIf the optional keyword `zlib` is `True`, the data will be compressed in\nthe netCDF file using gzip compression (default `False`).\n\nThe optional keyword `complevel` is an integer between 1 and 9 describing\nthe level of compression desired (default 4). Ignored if `zlib=False`.\n\nIf the optional keyword `shuffle` is `True`, the HDF5 shuffle filter\nwill be applied before compressing the data (default `True`).  This\nsignificantly improves compression. Default is `True`. Ignored if\n`zlib=False`.\n\nIf the optional keyword `fletcher32` is `True`, the Fletcher32 HDF5\nchecksum algorithm is activated to detect errors. Default `False`.\n\nIf the optional keyword `contiguous` is `True`, the variable data is\nstored contiguously on disk.  Default `False`. Setting to `True` for\na variable with an unlimited dimension will trigger an error.\n\nThe optional keyword `chunksizes` can be used to manually specify the\nHDF5 chunksizes for each dimension of the variable. A detailed\ndiscussion of HDF chunking and I/O performance is available\n[here](http://www.hdfgroup.org/HDF5/doc/H5.user/Chunking.html).\nBasically, you want the chunk size for each dimension to match as\nclosely as possible the size of the data block that users will read\nfrom the file.  `chunksizes` cannot be set if `contiguous=True`.\n\nThe optional keyword `endian` can be used to control whether the\ndata is stored in little or big endian format on disk. Possible\nvalues are `little, big` or `native` (default). The library\nwill automatically handle endian conversions when the data is read,\nbut if the data is always going to be read on a computer with the\nopposite format as the one used to create the file, there may be\nsome performance advantage to be gained by setting the endian-ness.\n\nThe `zlib, complevel, shuffle, fletcher32, contiguous, chunksizes` and `endian`\nkeywords are silently ignored for netCDF 3 files that do not use HDF5.\n\nThe optional keyword `fill_value` can be used to override the default\nnetCDF `_FillValue` (the value that the variable gets filled with before\nany data is written to it, defaults given in `netCDF4.default_fillvals`).\nIf fill_value is set to `False`, then the variable is not pre-filled.\n\nIf the optional keyword parameter `least_significant_digit` is\nspecified, variable data will be truncated (quantized). In conjunction\nwith `zlib=True` this produces \'lossy\', but significantly more\nefficient compression. For example, if `least_significant_digit=1`,\ndata will be quantized using `numpy.around(scale*data)/scale`, where\nscale = 2**bits, and bits is determined so that a precision of 0.1 is\nretained (in this case bits=4). From the \n[PSD metadata conventions](http://www.esrl.noaa.gov/psd/data/gridded/conventions/cdc_netcdf_standard.shtml):\n"least_significant_digit -- power of ten of the smallest decimal place\nin unpacked data that is a reliable value." Default is `None`, or no\nquantization, or \'lossless\' compression.\n\nWhen creating variables in a `NETCDF4` or `NETCDF4_CLASSIC` formatted file,\nHDF5 creates something called a \'chunk cache\' for each variable.  The\ndefault size of the chunk cache may be large enough to completely fill\navailable memory when creating thousands of variables.  The optional\nkeyword `chunk_cache` allows you to reduce (or increase) the size of\nthe default chunk cache when creating a variable.  The setting only\npersists as long as the Dataset is open - you can use the set_var_chunk_cache\nmethod to change it the next time the Dataset is opened.\nWarning - messing with this parameter can seriously degrade performance.\n\nThe return value is the `netCDF4.Variable` class instance describing the new\nvariable.\n\nA list of names corresponding to netCDF variable attributes can be\nobtained with the `netCDF4.Variable` method `netCDF4.Variable.ncattrs`. A dictionary\ncontaining all the netCDF attribute name/value pairs is provided by\nthe `__dict__` attribute of a `netCDF4.Variable` instance.\n\n`netCDF4.Variable` instances behave much like array objects. Data can be\nassigned to or retrieved from a variable with indexing and slicing\noperations on the `netCDF4.Variable` instance. A `netCDF4.Variable` instance has six\nDataset standard attributes: `dimensions, dtype, shape, ndim, name` and\n`least_significant_digit`. Application programs should never modify\nthese attributes. The `dimensions` attribute is a tuple containing the\nnames of the dimensions associated with this variable. The `dtype`\nattribute is a string describing the variable\'s data type (`i4, f8,\nS1,` etc). The `shape` attribute is a tuple describing the current\nsizes of all the variable\'s dimensions. The `name` attribute is a\nstring containing the name of the Variable instance.\nThe `least_significant_digit`\nattributes describes the power of ten of the smallest decimal place in\nthe data the contains a reliable value.  assigned to the `netCDF4.Variable`\ninstance. If `None`, the data is not truncated. The `ndim` attribute\nis the number of variable dimensions.'
        pass
    
    @property
    def data_model(self):
        pass
    
    def delncattr(self):
        '\n**`delncattr(self,name,value)`**\n\ndelete a netCDF dataset or group attribute.  Use if you need to delete a\nnetCDF attribute with the same name as one of the reserved python\nattributes.'
        pass
    
    @property
    def dimensions(self):
        pass
    
    @property
    def disk_format(self):
        pass
    
    @property
    def enumtypes(self):
        pass
    
    @property
    def file_format(self):
        pass
    
    def filepath(self):
        '\n**`filepath(self,encoding=None)`**\n\nGet the file system path (or the opendap URL) which was used to\nopen/create the Dataset. Requires netcdf >= 4.1.2.  The path\nis decoded into a string using `sys.getfilesystemencoding()` by default, this can be\nchanged using the `encoding` kwarg.'
        pass
    
    def get_variables_by_attributes(self):
        '\n**`get_variables_by_attribute(self, **kwargs)`**\n\nReturns a list of variables that match specific conditions.\n\nCan pass in key=value parameters and variables are returned that\ncontain all of the matches. For example, \n\n    :::python\n    >>> # Get variables with x-axis attribute.\n    >>> vs = nc.get_variables_by_attributes(axis=\'X\')\n    >>> # Get variables with matching "standard_name" attribute\n    >>> vs = nc.get_variables_by_attributes(standard_name=\'northward_sea_water_velocity\')\n\nCan pass in key=callable parameter and variables are returned if the\ncallable returns True.  The callable should accept a single parameter,\nthe attribute value.  None is given as the attribute value when the\nattribute does not exist on the variable. For example,\n\n    :::python\n    >>> # Get Axis variables\n    >>> vs = nc.get_variables_by_attributes(axis=lambda v: v in [\'X\', \'Y\', \'Z\', \'T\'])\n    >>> # Get variables that don\'t have an "axis" attribute\n    >>> vs = nc.get_variables_by_attributes(axis=lambda v: v is None)\n    >>> # Get variables that have a "grid_mapping" attribute\n    >>> vs = nc.get_variables_by_attributes(grid_mapping=lambda v: v is not None)\n'
        pass
    
    def getncattr(self):
        '\n**`getncattr(self,name)`**\n\nretrieve a netCDF dataset or group attribute.\nUse if you need to get a netCDF attribute with the same\nname as one of the reserved python attributes.\n\noption kwarg `encoding` can be used to specify the\ncharacter encoding of a string attribute (default is `utf-8`).'
        pass
    
    @property
    def groups(self):
        pass
    
    def isopen(self):
        '\n**`close(self)`**\n\nis the Dataset open or closed?\n        '
        pass
    
    @property
    def keepweakref(self):
        pass
    
    def ncattrs(self):
        '\n**`ncattrs(self)`**\n\nreturn netCDF global attribute names for this `netCDF4.Dataset` or `netCDF4.Group` in a list.'
        pass
    
    @property
    def parent(self):
        pass
    
    @property
    def path(self):
        pass
    
    def renameAttribute(self):
        '\n**`renameAttribute(self, oldname, newname)`**\n\nrename a `netCDF4.Dataset` or `netCDF4.Group` attribute named `oldname` to `newname`.'
        pass
    
    def renameDimension(self):
        '\n**`renameDimension(self, oldname, newname)`**\n\nrename a `netCDF4.Dimension` named `oldname` to `newname`.'
        pass
    
    def renameGroup(self):
        '\n**`renameGroup(self, oldname, newname)`**\n\nrename a `netCDF4.Group` named `oldname` to `newname` (requires netcdf >= 4.3.1).'
        pass
    
    def renameVariable(self):
        '\n**`renameVariable(self, oldname, newname)`**\n\nrename a `netCDF4.Variable` named `oldname` to `newname`'
        pass
    
    def set_always_mask(self):
        '\n**`set_always_mask(self, True_or_False)`**\n\nCall `netCDF4.Variable.set_always_mask` for all variables contained in\nthis `netCDF4.Dataset` or `netCDF4.Group`, as well as for all\nvariables in all its subgroups.\n\n**`True_or_False`**: Boolean determining if automatic conversion of\nmasked arrays with no missing values to regular ararys shall be\napplied for all variables.\n\n***Note***: Calling this function only affects existing\nvariables. Variables created after calling this function will follow\nthe default behaviour.\n        '
        pass
    
    def set_auto_chartostring(self):
        '\n**`set_auto_chartostring(self, True_or_False)`**\n\nCall `netCDF4.Variable.set_auto_chartostring` for all variables contained in this `netCDF4.Dataset` or\n`netCDF4.Group`, as well as for all variables in all its subgroups.\n\n**`True_or_False`**: Boolean determining if automatic conversion of\nall character arrays <--> string arrays should be performed for \ncharacter variables (variables of type `NC_CHAR` or `S1`) with the\n`_Encoding` attribute set.\n\n***Note***: Calling this function only affects existing variables. Variables created\nafter calling this function will follow the default behaviour.\n        '
        pass
    
    def set_auto_mask(self):
        '\n**`set_auto_mask(self, True_or_False)`**\n\nCall `netCDF4.Variable.set_auto_mask` for all variables contained in this `netCDF4.Dataset` or\n`netCDF4.Group`, as well as for all variables in all its subgroups.\n\n**`True_or_False`**: Boolean determining if automatic conversion to masked arrays\nshall be applied for all variables.\n\n***Note***: Calling this function only affects existing variables. Variables created\nafter calling this function will follow the default behaviour.\n        '
        pass
    
    def set_auto_maskandscale(self):
        '\n**`set_auto_maskandscale(self, True_or_False)`**\n\nCall `netCDF4.Variable.set_auto_maskandscale` for all variables contained in this `netCDF4.Dataset` or\n`netCDF4.Group`, as well as for all variables in all its subgroups.\n\n**`True_or_False`**: Boolean determining if automatic conversion to masked arrays\nand variable scaling shall be applied for all variables.\n\n***Note***: Calling this function only affects existing variables. Variables created\nafter calling this function will follow the default behaviour.\n        '
        pass
    
    def set_auto_scale(self):
        '\n**`set_auto_scale(self, True_or_False)`**\n\nCall `netCDF4.Variable.set_auto_scale` for all variables contained in this `netCDF4.Dataset` or\n`netCDF4.Group`, as well as for all variables in all its subgroups.\n\n**`True_or_False`**: Boolean determining if automatic variable scaling\nshall be applied for all variables.\n\n***Note***: Calling this function only affects existing variables. Variables created\nafter calling this function will follow the default behaviour.\n        '
        pass
    
    def set_fill_off(self):
        '\n**`set_fill_off(self)`**\n\nSets the fill mode for a `netCDF4.Dataset` open for writing to `off`.\n\nThis will prevent the data from being pre-filled with fill values, which\nmay result in some performance improvements. However, you must then make\nsure the data is actually written before being read.'
        pass
    
    def set_fill_on(self):
        "\n**`set_fill_on(self)`**\n\nSets the fill mode for a `netCDF4.Dataset` open for writing to `on`.\n\nThis causes data to be pre-filled with fill values. The fill values can be\ncontrolled by the variable's `_Fill_Value` attribute, but is usually\nsufficient to the use the netCDF default `_Fill_Value` (defined\nseparately for each variable type). The default behavior of the netCDF\nlibrary corresponds to `set_fill_on`.  Data which are equal to the\n`_Fill_Value` indicate that the variable was created, but never written\nto."
        pass
    
    def setncattr(self):
        '\n**`setncattr(self,name,value)`**\n\nset a netCDF dataset or group attribute using name,value pair.\nUse if you need to set a netCDF attribute with the\nwith the same name as one of the reserved python attributes.'
        pass
    
    def setncattr_string(self):
        '\n**`setncattr_string(self,name,value)`**\n\nset a netCDF dataset or group string attribute using name,value pair.\nUse if you need to ensure that a netCDF attribute is created with type\n`NC_STRING` if the file format is `NETCDF4`.'
        pass
    
    def setncatts(self):
        '\n**`setncatts(self,attdict)`**\n\nset a bunch of netCDF dataset or group attributes at once using a python dictionary.\nThis may be faster when setting a lot of attributes for a `NETCDF3`\nformatted file, since nc_redef/nc_enddef is not called in between setting\neach attribute'
        pass
    
    def sync(self):
        '\n**`sync(self)`**\n\nWrites all buffered data in the `netCDF4.Dataset` to the disk file.'
        pass
    
    @property
    def variables(self):
        pass
    
    @property
    def vltypes(self):
        pass
    

class Dimension(_mod_builtins.object):
    '\nA netCDF `netCDF4.Dimension` is used to describe the coordinates of a `netCDF4.Variable`.\nSee `netCDF4.Dimension.__init__` for more details.\n\nThe current maximum size of a `netCDF4.Dimension` instance can be obtained by\ncalling the python `len` function on the `netCDF4.Dimension` instance. The\n`netCDF4.Dimension.isunlimited` method of a `netCDF4.Dimension` instance can be used to\ndetermine if the dimension is unlimited.\n\nRead-only class variables:\n\n**`name`**: String name, used when creating a `netCDF4.Variable` with\n`netCDF4.Dataset.createVariable`.\n\n**`size`**: Current `netCDF4.Dimension` size (same as `len(d)`, where `d` is a\n`netCDF4.Dimension` instance).\n    '
    __class__ = Dimension
    def __init__(self):
        '\n        **`__init__(self, group, name, size=None)`**\n\n        `netCDF4.Dimension` constructor.\n\n        **`group`**: `netCDF4.Group` instance to associate with dimension.\n\n        **`name`**: Name of the dimension.\n\n        **`size`**: Size of the dimension. `None` or 0 means unlimited. (Default `None`).\n\n        ***Note***: `netCDF4.Dimension` instances should be created using the\n        `netCDF4.Dataset.createDimension` method of a `netCDF4.Group` or\n        `netCDF4.Dataset` instance, not using `netCDF4.Dimension.__init__` directly.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __unicode__(self):
        pass
    
    @property
    def _data_model(self):
        pass
    
    @property
    def _dimid(self):
        pass
    
    def _getname(self):
        pass
    
    @property
    def _grp(self):
        pass
    
    @property
    def _grpid(self):
        pass
    
    @property
    def _name(self):
        pass
    
    def group(self):
        '\n**`group(self)`**\n\nreturn the group that this `netCDF4.Dimension` is a member of.'
        pass
    
    def isunlimited(self):
        '\n**`isunlimited(self)`**\n\nreturns `True` if the `netCDF4.Dimension` instance is unlimited, `False` otherwise.'
        pass
    
    @property
    def name(self):
        'string name of Dimension instance'
        pass
    
    @property
    def size(self):
        'current size of Dimension (calls `len` on Dimension instance)'
        pass
    

class EnumType(_mod_builtins.object):
    '\nA `netCDF4.EnumType` instance is used to describe an Enum data\ntype, and can be passed to the the `netCDF4.Dataset.createVariable` method of\na `netCDF4.Dataset` or `netCDF4.Group` instance. See \n`netCDF4.EnumType.__init__` for more details.\n\nThe instance variables `dtype`, `name` and `enum_dict` should not be modified by\nthe user.\n    '
    __class__ = EnumType
    def __init__(self):
        '\n        **`__init__(group, datatype, datatype_name, enum_dict)`**\n\n        EnumType constructor.\n\n        **`group`**: `netCDF4.Group` instance to associate with the VLEN datatype.\n\n        **`datatype`**: An numpy integer dtype object describing the base type\n        for the Enum.\n\n        **`datatype_name`**: a Python string containing a description of the\n        Enum data type.\n\n        **`enum_dict`**: a Python dictionary containing the Enum field/value\n        pairs.\n\n        ***`Note`***: `netCDF4.EnumType` instances should be created using the\n        `netCDF4.Dataset.createEnumType`\n        method of a `netCDF4.Dataset` or `netCDF4.Group` instance, not using this class directly.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __unicode__(self):
        pass
    
    @property
    def _nc_type(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    @property
    def enum_dict(self):
        pass
    
    @property
    def name(self):
        pass
    

class Group(Dataset):
    "\nGroups define a hierarchical namespace within a netCDF file. They are\nanalogous to directories in a unix filesystem. Each `netCDF4.Group` behaves like\na `netCDF4.Dataset` within a Dataset, and can contain it's own variables,\ndimensions and attributes (and other Groups). See `netCDF4.Group.__init__`\nfor more details.\n\n`netCDF4.Group` inherits from `netCDF4.Dataset`, so all the \n`netCDF4.Dataset` class methods and variables are available\nto a `netCDF4.Group` instance (except the `close` method).\n\nAdditional read-only class variables:\n\n**`name`**: String describing the group name.\n    "
    __class__ = Group
    def __init__(self):
        '\n        **`__init__(self, parent, name)`**\n        `netCDF4.Group` constructor.\n\n        **`parent`**: `netCDF4.Group` instance for the parent group.  If being created\n        in the root group, use a `netCDF4.Dataset` instance.\n\n        **`name`**: - Name of the group.\n\n        ***Note***: `netCDF4.Group` instances should be created using the\n        `netCDF4.Dataset.createGroup` method of a `netCDF4.Dataset` instance, or\n        another `netCDF4.Group` instance, not using this class directly.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def _getname(self):
        pass
    
    def close(self):
        '\n**`close(self)`**\n\noverrides `netCDF4.Dataset` close method which does not apply to `netCDF4.Group`\ninstances, raises IOError.'
        pass
    
    @property
    def name(self):
        'string name of Group instance'
        pass
    

class MFDataset(Dataset):
    '\nClass for reading multi-file netCDF Datasets, making variables\nspanning multiple files appear as if they were in one file.\nDatasets must be in `NETCDF4_CLASSIC, NETCDF3_CLASSIC, NETCDF3_64BIT_OFFSET\nor NETCDF3_64BIT_DATA` format (`NETCDF4` Datasets won\'t work).\n\nAdapted from [pycdf](http://pysclint.sourceforge.net/pycdf) by Andre Gosselin.\n\nExample usage (See `netCDF4.MFDataset.__init__` for more details):\n\n    :::python\n    >>> import numpy as np\n    >>> # create a series of netCDF files with a variable sharing\n    >>> # the same unlimited dimension.\n    >>> for nf in range(10):\n    >>>     f = Dataset("mftest%s.nc" % nf,"w",format=\'NETCDF4_CLASSIC\')\n    >>>     f.createDimension("x",None)\n    >>>     x = f.createVariable("x","i",("x",))\n    >>>     x[0:10] = np.arange(nf*10,10*(nf+1))\n    >>>     f.close()\n    >>> # now read all those files in at once, in one Dataset.\n    >>> f = MFDataset("mftest*nc")\n    >>> print f.variables["x"][:]\n    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24\n     25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49\n     50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74\n     75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]\n    '
    __class__ = MFDataset
    __dict__ = {}
    def __getattribute__(self, name):
        pass
    
    def __init__(self, files, check, aggdim, exclude, master_file):
        '\n        **`__init__(self, files, check=False, aggdim=None, exclude=[],\n        master_file=None)`**\n\n        Open a Dataset spanning multiple files, making it look as if it was a\n        single file. Variables in the list of files that share the same\n        dimension (specified with the keyword `aggdim`) are aggregated. If\n        `aggdim` is not specified, the unlimited is aggregated.  Currently,\n        `aggdim` must be the leftmost (slowest varying) dimension of each\n        of the variables to be aggregated.\n        \n        **`files`**: either a sequence of netCDF files or a string with a\n        wildcard (converted to a sorted list of files using glob)  If\n        the `master_file` kwarg is not specified, the first file\n        in the list will become the "master" file, defining all the\n        variables with an aggregation dimension which may span\n        subsequent files. Attribute access returns attributes only from "master"\n        file. The files are always opened in read-only mode.\n        \n        **`check`**: True if you want to do consistency checking to ensure the\n        correct variables structure for all of the netcdf files.  Checking makes\n        the initialization of the MFDataset instance much slower. Default is\n        False.\n        \n        **`aggdim`**: The name of the dimension to aggregate over (must\n        be the leftmost dimension of each of the variables to be aggregated).\n        If None (default), aggregate over the unlimited dimension.\n        \n        **`exclude`**: A list of variable names to exclude from aggregation.\n        Default is an empty list.\n\n        **`master_file`**: file to use as "master file", defining all the\n        variables with an aggregation dimension and all global attributes.\n       '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        return ''
    
    def __setattr__(self, name, value):
        'override base class attribute creation'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def close(self):
        '\n        **`close(self)`**\n\n        close all the open files.\n        '
        pass
    
    def ncattrs(self):
        '\n        **`ncattrs(self)`**\n\n        return the netcdf attribute names from the master file.\n        '
        pass
    

class MFTime(_Variable):
    '\nClass providing an interface to a MFDataset time Variable by imposing a unique common\ntime unit and/or calendar to all files.\n\nExample usage (See `netCDF4.MFTime.__init__` for more details):\n\n    :::python\n    >>> import numpy\n    >>> f1 = Dataset("mftest_1.nc","w", format="NETCDF4_CLASSIC")\n    >>> f2 = Dataset("mftest_2.nc","w", format="NETCDF4_CLASSIC")\n    >>> f1.createDimension("time",None)\n    >>> f2.createDimension("time",None)\n    >>> t1 = f1.createVariable("time","i",("time",))\n    >>> t2 = f2.createVariable("time","i",("time",))\n    >>> t1.units = "days since 2000-01-01"\n    >>> t2.units = "days since 2000-02-01"\n    >>> t1.calendar = "standard"\n    >>> t2.calendar = "standard"\n    >>> t1[:] = numpy.arange(31)\n    >>> t2[:] = numpy.arange(30)\n    >>> f1.close()\n    >>> f2.close()\n    >>> # Read the two files in at once, in one Dataset.\n    >>> f = MFDataset("mftest*nc")\n    >>> t = f.variables["time"]\n    >>> print t.units\n    days since 2000-01-01\n    >>> print t[32] # The value written in the file, inconsistent with the MF time units.\n    1\n    >>> T = MFTime(t)\n    >>> print T[32]\n    32\n    '
    __class__ = MFTime
    __dict__ = {}
    def __getitem__(self, elem):
        pass
    
    def __init__(self, time, units, calendar):
        "\n        **`__init__(self, time, units=None, calendar=None)`**\n\n        Create a time Variable with units consistent across a multifile\n        dataset.\n        \n        **`time`**: Time variable from a `netCDF4.MFDataset`.\n        \n        **`units`**: Time units, for example, `'days since 1979-01-01'`. If `None`,\n        use the units from the master variable.\n\n        **`calendar`**: Calendar overload to use across all files, for example,\n        `'standard'` or `'gregorian'`. If `None`, check that the calendar attribute\n        is present on each variable and values are unique across files raising a\n        `ValueError` otherwise.\n        "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

NC_DISKLESS = 8
OrderedDict = _mod_collections.OrderedDict
class VLType(_mod_builtins.object):
    '\nA `netCDF4.VLType` instance is used to describe a variable length (VLEN) data\ntype, and can be passed to the the `netCDF4.Dataset.createVariable` method of\na `netCDF4.Dataset` or `netCDF4.Group` instance. See \n`netCDF4.VLType.__init__` for more details.\n\nThe instance variables `dtype` and `name` should not be modified by\nthe user.\n    '
    __class__ = VLType
    def __init__(self):
        '\n        **`__init__(group, datatype, datatype_name)`**\n\n        VLType constructor.\n\n        **`group`**: `netCDF4.Group` instance to associate with the VLEN datatype.\n\n        **`datatype`**: An numpy dtype object describing the component type for the\n        variable length array.\n\n        **`datatype_name`**: a Python string containing a description of the\n        VLEN data type.\n\n        ***`Note`***: `netCDF4.VLType` instances should be created using the\n        `netCDF4.Dataset.createVLType`\n        method of a `netCDF4.Dataset` or `netCDF4.Group` instance, not using this class directly.\n        '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __unicode__(self):
        pass
    
    @property
    def _nc_type(self):
        pass
    
    @property
    def dtype(self):
        pass
    
    @property
    def name(self):
        pass
    

class Variable(_mod_builtins.object):
    "\nA netCDF `netCDF4.Variable` is used to read and write netCDF data.  They are\nanalogous to numpy array objects. See `netCDF4.Variable.__init__` for more\ndetails.\n\nA list of attribute names corresponding to netCDF attributes defined for\nthe variable can be obtained with the `netCDF4.Variable.ncattrs` method. These\nattributes can be created by assigning to an attribute of the\n`netCDF4.Variable` instance. A dictionary containing all the netCDF attribute\nname/value pairs is provided by the `__dict__` attribute of a\n`netCDF4.Variable` instance.\n\nThe following class variables are read-only:\n\n**`dimensions`**: A tuple containing the names of the\ndimensions associated with this variable.\n\n**`dtype`**: A numpy dtype object describing the\nvariable's data type.\n\n**`ndim`**: The number of variable dimensions.\n\n**`shape`**: A tuple with the current shape (length of all dimensions).\n\n**`scale`**: If True, `scale_factor` and `add_offset` are\napplied, and signed integer data is automatically converted to\nunsigned integer data if the `_Unsigned` attribute is set. \nDefault is `True`, can be reset using `netCDF4.Variable.set_auto_scale` and\n`netCDF4.Variable.set_auto_maskandscale` methods.\n\n**`mask`**: If True, data is automatically converted to/from masked \narrays when missing values or fill values are present. Default is `True`, can be\nreset using `netCDF4.Variable.set_auto_mask` and `netCDF4.Variable.set_auto_maskandscale`\nmethods.\n\n**`chartostring`**: If True, data is automatically converted to/from character \narrays to string arrays when the `_Encoding` variable attribute is set. \nDefault is `True`, can be reset using\n`netCDF4.Variable.set_auto_chartostring` method.\n\n**`least_significant_digit`**: Describes the power of ten of the \nsmallest decimal place in the data the contains a reliable value.  Data is\ntruncated to this decimal place when it is assigned to the `netCDF4.Variable`\ninstance. If `None`, the data is not truncated.\n\n**`__orthogonal_indexing__`**: Always `True`.  Indicates to client code\nthat the object supports 'orthogonal indexing', which means that slices\nthat are 1d arrays or lists slice along each dimension independently.  This\nbehavior is similar to Fortran or Matlab, but different than numpy.\n\n**`datatype`**: numpy data type (for primitive data types) or VLType/CompoundType\n instance (for compound or vlen data types).\n\n**`name`**: String name.\n\n**`size`**: The number of stored elements.\n    "
    def __array__(self):
        pass
    
    __class__ = Variable
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getattr__(self):
        pass
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __init__(self):
        "\n        **`__init__(self, group, name, datatype, dimensions=(), zlib=False,\n        complevel=4, shuffle=True, fletcher32=False, contiguous=False,\n        chunksizes=None, endian='native',\n        least_significant_digit=None,fill_value=None)`**\n\n        `netCDF4.Variable` constructor.\n\n        **`group`**: `netCDF4.Group` or `netCDF4.Dataset` instance to associate with variable.\n\n        **`name`**: Name of the variable.\n\n        **`datatype`**: `netCDF4.Variable` data type. Can be specified by providing a\n        numpy dtype object, or a string that describes a numpy dtype object.\n        Supported values, corresponding to `str` attribute of numpy dtype\n        objects, include `'f4'` (32-bit floating point), `'f8'` (64-bit floating\n        point), `'i4'` (32-bit signed integer), `'i2'` (16-bit signed integer),\n        `'i8'` (64-bit signed integer), `'i4'` (8-bit signed integer), `'i1'`\n        (8-bit signed integer), `'u1'` (8-bit unsigned integer), `'u2'` (16-bit\n        unsigned integer), `'u4'` (32-bit unsigned integer), `'u8'` (64-bit\n        unsigned integer), or `'S1'` (single-character string).  From\n        compatibility with Scientific.IO.NetCDF, the old Numeric single character\n        typecodes can also be used (`'f'` instead of `'f4'`, `'d'` instead of\n        `'f8'`, `'h'` or `'s'` instead of `'i2'`, `'b'` or `'B'` instead of\n        `'i1'`, `'c'` instead of `'S1'`, and `'i'` or `'l'` instead of\n        `'i4'`). `datatype` can also be a `netCDF4.CompoundType` instance\n        (for a structured, or compound array), a `netCDF4.VLType` instance\n        (for a variable-length array), or the python `str` builtin\n        (for a variable-length string array). Numpy string and unicode datatypes with\n        length greater than one are aliases for `str`.\n        \n        **`dimensions`**: a tuple containing the variable's dimension names\n        (defined previously with `createDimension`). Default is an empty tuple\n        which means the variable is a scalar (and therefore has no dimensions).\n        \n        **`zlib`**: if `True`, data assigned to the `netCDF4.Variable`\n        instance is compressed on disk. Default `False`.\n        \n        **`complevel`**: the level of zlib compression to use (1 is the fastest,\n        but poorest compression, 9 is the slowest but best compression). Default 4.\n        Ignored if `zlib=False`.\n        \n        **`shuffle`**: if `True`, the HDF5 shuffle filter is applied\n        to improve compression. Default `True`. Ignored if `zlib=False`.\n        \n        **`fletcher32`**: if `True` (default `False`), the Fletcher32 checksum\n        algorithm is used for error detection.\n        \n        **`contiguous`**: if `True` (default `False`), the variable data is\n        stored contiguously on disk.  Default `False`. Setting to `True` for\n        a variable with an unlimited dimension will trigger an error.\n        \n        **`chunksizes`**: Can be used to specify the HDF5 chunksizes for each\n        dimension of the variable. A detailed discussion of HDF chunking and I/O\n        performance is available\n        [here](http://www.hdfgroup.org/HDF5/doc/H5.user/Chunking.html).\n        Basically, you want the chunk size for each dimension to match as\n        closely as possible the size of the data block that users will read\n        from the file. `chunksizes` cannot be set if `contiguous=True`.\n        \n        **`endian`**: Can be used to control whether the\n        data is stored in little or big endian format on disk. Possible\n        values are `little, big` or `native` (default). The library\n        will automatically handle endian conversions when the data is read,\n        but if the data is always going to be read on a computer with the\n        opposite format as the one used to create the file, there may be\n        some performance advantage to be gained by setting the endian-ness.\n        For netCDF 3 files (that don't use HDF5), only `endian='native'` is allowed.\n        \n        The `zlib, complevel, shuffle, fletcher32, contiguous` and `chunksizes`\n        keywords are silently ignored for netCDF 3 files that do not use HDF5.\n        \n        **`least_significant_digit`**: If specified, variable data will be\n        truncated (quantized). In conjunction with `zlib=True` this produces\n        'lossy', but significantly more efficient compression. For example, if\n        `least_significant_digit=1`, data will be quantized using\n        around(scale*data)/scale, where scale = 2**bits, and bits is determined\n        so that a precision of 0.1 is retained (in this case bits=4). Default is\n        `None`, or no quantization.\n        \n        **`fill_value`**:  If specified, the default netCDF `_FillValue` (the\n        value that the variable gets filled with before any data is written to it)\n        is replaced with this value.  If fill_value is set to `False`, then\n        the variable is not pre-filled. The default netCDF fill values can be found\n        in `netCDF4.default_fillvals`.\n\n        ***Note***: `netCDF4.Variable` instances should be created using the\n        `netCDF4.Dataset.createVariable` method of a `netCDF4.Dataset` or\n        `netCDF4.Group` instance, not using this class directly.\n        "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    @property
    def __orthogonal_indexing__(self):
        pass
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __unicode__(self):
        pass
    
    def _assign_vlen(self):
        'private method to assign data to a single item in a VLEN variable'
        pass
    
    def _check_safecast(self):
        pass
    
    @property
    def _cmptype(self):
        pass
    
    @property
    def _enumtype(self):
        pass
    
    def _get(self):
        'Private method to retrieve data from a netCDF variable'
        pass
    
    def _getdims(self):
        pass
    
    def _getname(self):
        pass
    
    @property
    def _grp(self):
        pass
    
    @property
    def _grpid(self):
        pass
    
    @property
    def _has_lsd(self):
        pass
    
    @property
    def _iscompound(self):
        pass
    
    @property
    def _isenum(self):
        pass
    
    @property
    def _isprimitive(self):
        pass
    
    @property
    def _isvlen(self):
        pass
    
    @property
    def _name(self):
        pass
    
    @property
    def _no_get_vars(self):
        pass
    
    @property
    def _nunlimdim(self):
        pass
    
    def _put(self):
        'Private method to put data into a netCDF variable'
        pass
    
    def _toma(self):
        pass
    
    @property
    def _varid(self):
        pass
    
    @property
    def _vltype(self):
        pass
    
    @property
    def always_mask(self):
        pass
    
    def assignValue(self):
        '\n**`assignValue(self, val)`**\n\nassign a value to a scalar variable.  Provided for compatibility with\nScientific.IO.NetCDF, can also be done by assigning to an Ellipsis slice ([...]).'
        pass
    
    @property
    def chartostring(self):
        pass
    
    def chunking(self):
        "\n**`chunking(self)`**\n\nreturn variable chunking information.  If the dataset is\ndefined to be contiguous (and hence there is no chunking) the word 'contiguous'\nis returned.  Otherwise, a sequence with the chunksize for\neach dimension is returned."
        pass
    
    @property
    def datatype(self):
        'numpy data type (for primitive data types) or\n        VLType/CompoundType/EnumType instance \n        (for compound, vlen  or enum data types)'
        pass
    
    def delncattr(self):
        '\n**`delncattr(self,name,value)`**\n\ndelete a netCDF variable attribute.  Use if you need to delete a\nnetCDF attribute with the same name as one of the reserved python\nattributes.'
        pass
    
    @property
    def dimensions(self):
        "get variables's dimension names"
        pass
    
    @property
    def dtype(self):
        pass
    
    def endian(self):
        '\n**`endian(self)`**\n\nreturn endian-ness (`little,big,native`) of variable (as stored in HDF5 file).'
        pass
    
    def filters(self):
        '\n**`filters(self)`**\n\nreturn dictionary containing HDF5 filter parameters.'
        pass
    
    def getValue(self):
        '\n**`getValue(self)`**\n\nget the value of a scalar variable.  Provided for compatibility with\nScientific.IO.NetCDF, can also be done by slicing with an Ellipsis ([...]).'
        pass
    
    def get_dims(self):
        '\n**`get_dims(self)`**\n\nreturn a tuple of `netCDF4.Dimension` instances associated with this \n`netCDF4.Variable.\n        '
        pass
    
    def get_var_chunk_cache(self):
        '\n**`get_var_chunk_cache(self)`**\n\nreturn variable chunk cache information in a tuple (size,nelems,preemption).\nSee netcdf C library documentation for `nc_get_var_chunk_cache` for\ndetails.'
        pass
    
    def getncattr(self):
        '\n**`getncattr(self,name)`**\n\nretrieve a netCDF variable attribute.  Use if you need to set a\nnetCDF attribute with the same name as one of the reserved python\nattributes.\n\noption kwarg `encoding` can be used to specify the\ncharacter encoding of a string attribute (default is `utf-8`).'
        pass
    
    def group(self):
        '\n**`group(self)`**\n\nreturn the group that this `netCDF4.Variable` is a member of.'
        pass
    
    @property
    def mask(self):
        pass
    
    @property
    def name(self):
        'string name of Variable instance'
        pass
    
    def ncattrs(self):
        '\n**`ncattrs(self)`**\n\nreturn netCDF attribute names for this `netCDF4.Variable` in a list.'
        pass
    
    @property
    def ndim(self):
        pass
    
    def renameAttribute(self):
        '\n**`renameAttribute(self, oldname, newname)`**\n\nrename a `netCDF4.Variable` attribute named `oldname` to `newname`.'
        pass
    
    @property
    def scale(self):
        pass
    
    def set_always_mask(self):
        '\n**`set_always_mask(self,always_mask)`**\n\nturn on or off conversion of data without missing values to regular\nnumpy arrays.\n\nIf `always_mask` is set to `True` then a masked array with no missing\nvalues is converted to a regular numpy array.\n\nThe default value of `always_mask` is `True` (conversions to regular\nnumpy arrays are not performed).\n\n        '
        pass
    
    def set_auto_chartostring(self):
        '\n**`set_auto_chartostring(self,chartostring)`**\n\nturn on or off automatic conversion of character variable data to and\nfrom numpy fixed length string arrays when the `_Encoding` variable attribute\nis set.\n\nIf `chartostring` is set to `True`, when data is read from a character variable\n(dtype = `S1`) that has an `_Encoding` attribute, it is converted to a numpy\nfixed length unicode string array (dtype = `UN`, where `N` is the length\nof the the rightmost dimension of the variable).  The value of `_Encoding`\nis the unicode encoding that is used to decode the bytes into strings. \n\nWhen numpy string data is written to a variable it is converted back to\nindiviual bytes, with the number of bytes in each string equalling the\nrightmost dimension of the variable.\n\nThe default value of `chartostring` is `True`\n(automatic conversions are performed).\n        '
        pass
    
    def set_auto_mask(self):
        '\n**`set_auto_mask(self,mask)`**\n\nturn on or off automatic conversion of variable data to and\nfrom masked arrays .\n\nIf `mask` is set to `True`, when data is read from a variable\nit is converted to a masked array if any of the values are exactly\nequal to the either the netCDF _FillValue or the value specified by the\nmissing_value variable attribute. The fill_value of the masked array\nis set to the missing_value attribute (if it exists), otherwise\nthe netCDF _FillValue attribute (which has a default value\nfor each data type).  When data is written to a variable, the masked\narray is converted back to a regular numpy array by replacing all the\nmasked values by the missing_value attribute of the variable (if it\nexists).  If the variable has no missing_value attribute, the _FillValue\nis used instead. If the variable has valid_min/valid_max and \nmissing_value attributes, data outside the specified range will be\nset to missing_value.\n\nThe default value of `mask` is `True`\n(automatic conversions are performed).\n        '
        pass
    
    def set_auto_maskandscale(self):
        '\n**`set_auto_maskandscale(self,maskandscale)`**\n\nturn on or off automatic conversion of variable data to and\nfrom masked arrays, automatic packing/unpacking of variable\ndata using `scale_factor` and `add_offset` attributes and \nautomatic conversion of signed integer data to unsigned integer\ndata if the `_Unsigned` attribute exists.\n\nIf `maskandscale` is set to `True`, when data is read from a variable\nit is converted to a masked array if any of the values are exactly\nequal to the either the netCDF _FillValue or the value specified by the\nmissing_value variable attribute. The fill_value of the masked array\nis set to the missing_value attribute (if it exists), otherwise\nthe netCDF _FillValue attribute (which has a default value\nfor each data type).  When data is written to a variable, the masked\narray is converted back to a regular numpy array by replacing all the\nmasked values by the missing_value attribute of the variable (if it\nexists).  If the variable has no missing_value attribute, the _FillValue\nis used instead. If the variable has valid_min/valid_max and \nmissing_value attributes, data outside the specified range will be\nset to missing_value.\n\nIf `maskandscale` is set to `True`, and the variable has a\n`scale_factor` or an `add_offset` attribute, then data read\nfrom that variable is unpacked using::\n\n    data = self.scale_factor*data + self.add_offset\n\nWhen data is written to a variable it is packed using::\n\n    data = (data - self.add_offset)/self.scale_factor\n\nIf either scale_factor is present, but add_offset is missing, add_offset\nis assumed zero.  If add_offset is present, but scale_factor is missing,\nscale_factor is assumed to be one.\nFor more information on how `scale_factor` and `add_offset` can be\nused to provide simple compression, see the\n[PSD metadata conventions](http://www.esrl.noaa.gov/psd/data/gridded/conventions/cdc_netcdf_standard.shtml).\n\nIn addition, if `maskandscale` is set to `True`, and if the variable has an \nattribute `_Unsigned` set, and the variable has a signed integer data type, \na view to the data is returned with the corresponding unsigned integer data type.\nThis convention is used by the netcdf-java library to save unsigned integer\ndata in `NETCDF3` or `NETCDF4_CLASSIC` files (since the `NETCDF3` \ndata model does not have unsigned integer data types).\n\nThe default value of `maskandscale` is `True`\n(automatic conversions are performed).\n        '
        pass
    
    def set_auto_scale(self):
        '\n**`set_auto_scale(self,scale)`**\n\nturn on or off automatic packing/unpacking of variable\ndata using `scale_factor` and `add_offset` attributes.\nAlso turns on and off automatic conversion of signed integer data\nto unsigned integer data if the variable has an `_Unsigned`\nattribute.\n\nIf `scale` is set to `True`, and the variable has a\n`scale_factor` or an `add_offset` attribute, then data read\nfrom that variable is unpacked using::\n\n    data = self.scale_factor*data + self.add_offset\n\nWhen data is written to a variable it is packed using::\n\n    data = (data - self.add_offset)/self.scale_factor\n\nIf either scale_factor is present, but add_offset is missing, add_offset\nis assumed zero.  If add_offset is present, but scale_factor is missing,\nscale_factor is assumed to be one.\nFor more information on how `scale_factor` and `add_offset` can be\nused to provide simple compression, see the\n[PSD metadata conventions](http://www.esrl.noaa.gov/psd/data/gridded/conventions/cdc_netcdf_standard.shtml).\n\nIn addition, if `scale` is set to `True`, and if the variable has an \nattribute `_Unsigned` set, and the variable has a signed integer data type,\na view to the data is returned with the corresponding unsigned integer datatype.\nThis convention is used by the netcdf-java library to save unsigned integer\ndata in `NETCDF3` or `NETCDF4_CLASSIC` files (since the `NETCDF3` \ndata model does not have unsigned integer data types).\n\nThe default value of `scale` is `True`\n(automatic conversions are performed).\n        '
        pass
    
    def set_collective(self):
        '\n**`set_collective(self,True_or_False)`**\n\nturn on or off collective parallel IO access. Ignored if file is not\nopen for parallel access.\n        '
        pass
    
    def set_var_chunk_cache(self):
        '\n**`set_var_chunk_cache(self,size=None,nelems=None,preemption=None)`**\n\nchange variable chunk cache settings.\nSee netcdf C library documentation for `nc_set_var_chunk_cache` for\ndetails.'
        pass
    
    def setncattr(self):
        '\n**`setncattr(self,name,value)`**\n\nset a netCDF variable attribute using name,value pair.  Use if you need to set a\nnetCDF attribute with the same name as one of the reserved python\nattributes.'
        pass
    
    def setncattr_string(self):
        '\n**`setncattr_string(self,name,value)`**\n\nset a netCDF variable string attribute using name,value pair.\nUse if you need to ensure that a netCDF attribute is created with type\n`NC_STRING` if the file format is `NETCDF4`.\nUse if you need to set an attribute to an array of variable-length strings.'
        pass
    
    def setncatts(self):
        '\n**`setncatts(self,attdict)`**\n\nset a bunch of netCDF variable attributes at once using a python dictionary.\nThis may be faster when setting a lot of attributes for a `NETCDF3`\nformatted file, since nc_redef/nc_enddef is not called in between setting\neach attribute'
        pass
    
    @property
    def shape(self):
        'find current sizes of all variable dimensions'
        pass
    
    @property
    def size(self):
        'Return the number of stored elements.'
        pass
    
    def use_nc_get_vars(self):
        '\n**`use_nc_get_vars(self,_no_get_vars)`**\n\nenable the use of netcdf library routine `nc_get_vars`\nto retrieve strided variable slices.  By default,\n`nc_get_vars` may not used by default (depending on the\nversion of the netcdf-c library being used) since it may be\nslower than multiple calls to the unstrided read routine `nc_get_vara`.\n        '
        pass
    

class _Dimension(_mod_builtins.object):
    __class__ = _Dimension
    __dict__ = {}
    def __init__(self, dimname, dim, dimlens, dimtotlen):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        return 0
    
    __module__ = 'netCDF4._netCDF4'
    def __repr__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def isunlimited(self):
        pass
    

def _StartCountStride(elem, shape, dimensions, grp, datashape, put, no_get_vars):
    'Return start, count, stride and indices needed to store/extract data\n    into/from a netCDF variable.\n\n    This function is used to convert a slicing expression into a form that is\n    compatible with the nc_get_vars function. Specifically, it needs\n    to interpret integers, slices, Ellipses, and 1-d sequences of integers\n    and booleans.\n\n    Numpy uses "broadcasting indexing" to handle array-valued indices.\n    "Broadcasting indexing" (a.k.a "fancy indexing") treats all multi-valued\n    indices together to allow arbitrary points to be extracted. The index\n    arrays can be multidimensional, and more than one can be specified in a\n    slice, as long as they can be "broadcast" against each other.\n    This style of indexing can be very powerful, but it is very hard\n    to understand, explain, and implement (and can lead to hard to find bugs).\n    Most other python packages and array processing\n    languages (such as netcdf4-python, xray, biggus, matlab and fortran)\n    use "orthogonal indexing" which only allows for 1-d index arrays and\n    treats these arrays of indices independently along each dimension.\n\n    The implementation of "orthogonal indexing" used here requires that\n    index arrays be 1-d boolean or integer. If integer arrays are used,\n    the index values must be sorted and contain no duplicates.\n\n    In summary, slicing netcdf4-python variable objects with 1-d integer or\n    boolean arrays is allowed, but may give a different result than slicing a\n    numpy array.\n\n    Numpy also supports slicing an array with a boolean array of the same\n    shape. For example x[x>0] returns a 1-d array with all the positive values of x.\n    This is also not supported in netcdf4-python, if x.ndim > 1.\n\n    Orthogonal indexing can be used in to select netcdf variable slices\n    using the dimension variables. For example, you can use v[lat>60,lon<180]\n    to fetch the elements of v obeying conditions on latitude and longitude.\n    Allow for this sort of simple variable subsetting is the reason we decided to\n    deviate from numpy\'s slicing rules.\n\n    This function is used both by the __setitem__ and __getitem__ method of\n    the Variable class.\n\n    Parameters\n    ----------\n    elem : tuple of integer, slice, ellipsis or 1-d boolean or integer\n    sequences used to slice the netCDF Variable (Variable[elem]).\n    shape : tuple containing the current shape of the netCDF variable.\n    dimensions : sequence\n      The name of the dimensions.\n      __setitem__.\n    grp  : netCDF Group\n      The netCDF group to which the variable being set belongs to.\n    datashape : sequence\n      The shape of the data that is being stored. Only needed by __setitime__\n    put : True|False (default False).  If called from __setitem__, put is True.\n\n    Returns\n    -------\n    start : ndarray (..., n)\n      A starting indices array of dimension n+1. The first n\n      dimensions identify different independent data chunks. The last dimension\n      can be read as the starting indices.\n    count : ndarray (..., n)\n      An array of dimension (n+1) storing the number of elements to get.\n    stride : ndarray (..., n)\n      An array of dimension (n+1) storing the steps between each datum.\n    indices : ndarray (..., n)\n      An array storing the indices describing the location of the\n      data chunk in the target/source array (__getitem__/__setitem__).\n\n    Notes:\n\n    netCDF data is accessed via the function:\n       nc_get_vars(grpid, varid, start, count, stride, data)\n\n    Assume that the variable has dimension n, then\n\n    start is a n-tuple that contains the indices at the beginning of data chunk.\n    count is a n-tuple that contains the number of elements to be accessed.\n    stride is a n-tuple that contains the step length between each element.\n\n    '
    pass

class _Variable(_mod_builtins.object):
    __class__ = _Variable
    __dict__ = {}
    def __getattr__(self, name):
        pass
    
    def __getitem__(self, elem):
        'Get records from a concatenated set of variables.'
        pass
    
    def __init__(self, dset, varname, var, recdimname):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        return 0
    
    __module__ = 'netCDF4._netCDF4'
    def __repr__(self):
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def _shape(self):
        pass
    
    def ncattrs(self):
        pass
    
    def set_auto_chartostring(self, val):
        pass
    
    def set_auto_mask(self, val):
        pass
    
    def set_auto_maskandscale(self, val):
        pass
    
    def set_auto_scale(self, val):
        pass
    
    def typecode(self):
        pass
    

__builtins__ = {}
__doc__ = '\nVersion 1.4.2\n-------------\n- - - \n\nIntroduction\n============\n\nnetcdf4-python is a Python interface to the netCDF C library.  \n\n[netCDF](http://www.unidata.ucar.edu/software/netcdf/) version 4 has many features\nnot found in earlier versions of the library and is implemented on top of\n[HDF5](http://www.hdfgroup.org/HDF5). This module can read and write\nfiles in both the new netCDF 4 and the old netCDF 3 format, and can create\nfiles that are readable by HDF5 clients. The API modelled after\n[Scientific.IO.NetCDF](http://dirac.cnrs-orleans.fr/ScientificPython/),\nand should be familiar to users of that module.\n\nMost new features of netCDF 4 are implemented, such as multiple\nunlimited dimensions, groups and zlib data compression.  All the new\nnumeric data types (such as 64 bit and unsigned integer types) are\nimplemented. Compound (struct), variable length (vlen) and\nenumerated (enum) data types are supported, but not the opaque data type.\nMixtures of compound, vlen and enum data types (such as\ncompound types containing enums, or vlens containing compound\ntypes) are not supported.\n\nDownload\n========\n\n - Latest bleeding-edge code from the \n   [github repository](http://github.com/Unidata/netcdf4-python).\n - Latest [releases](https://pypi.python.org/pypi/netCDF4)\n   (source code and binary installers).\n\nRequires\n========\n\n - Python 2.7 or later (python 3 works too).\n - [numpy array module](http://numpy.scipy.org), version 1.9.0 or later.\n - [Cython](http://cython.org), version 0.21 or later.\n - [setuptools](https://pypi.python.org/pypi/setuptools), version 18.0 or\n   later.\n - [cftime](https://github.com/Unidata/cftime) for \n the time and date handling utility functions (`netCDF4.num2date`,\n `netCDF4.date2num` and `netCDF4.date2index`).\n - The HDF5 C library version 1.8.4-patch1 or higher (1.8.x recommended)\n from [](ftp://ftp.hdfgroup.org/HDF5/current/src).\n ***netCDF version 4.4.1 or higher is recommended if using HDF5 1.10.x -\n otherwise resulting files may be unreadable by clients using earlier\n versions of HDF5.  For netCDF < 4.4.1, HDF5 version 1.8.x is recommended.***\n Be sure to build with `--enable-hl --enable-shared`.\n - [Libcurl](http://curl.haxx.se/libcurl), if you want\n [OPeNDAP](http://opendap.org) support.\n - [HDF4](http://www.hdfgroup.org/products/hdf4), if you want\n to be able to read HDF4 "Scientific Dataset" (SD) files.\n - The netCDF-4 C library from the [github releases\n   page](https://github.com/Unidata/netcdf-c/releases). \n Version 4.1.1 or higher is required (4.2 or higher recommended).\n Be sure to build with `--enable-netcdf-4 --enable-shared`, and set\n `CPPFLAGS="-I $HDF5_DIR/include"` and `LDFLAGS="-L $HDF5_DIR/lib"`,\n where `$HDF5_DIR` is the directory where HDF5 was installed.\n If you want [OPeNDAP](http://opendap.org) support, add `--enable-dap`.\n If you want HDF4 SD support, add `--enable-hdf4` and add\n the location of the HDF4 headers and library to `$CPPFLAGS` and `$LDFLAGS`.\n - for MPI parallel IO support, MPI-enabled versions of the HDF5 and netcdf\n libraries are required, as is the [mpi4py](http://mpi4py.scipy.org) python\n module.\n\n\nInstall\n=======\n\n - install the requisite python modules and C libraries (see above). It\'s\n easiest if all the C libs are built as shared libraries.\n - By default, the utility `nc-config`, installed with netcdf 4.1.2 or higher,\n will be run used to determine where all the dependencies live.\n - If `nc-config` is not in your default `$PATH`\n edit the `setup.cfg` file\n in a text editor and follow the instructions in the comments.\n In addition to specifying the path to `nc-config`,\n you can manually set the paths to all the libraries and their include files\n (in case `nc-config` does not do the right thing).\n - run `python setup.py build`, then `python setup.py install` (as root if\n necessary).\n - [`pip install`](https://pip.pypa.io/en/latest/reference/pip_install.html) can\n also be used, with library paths set with environment variables. To make\n this work, the `USE_SETUPCFG` environment variable must be used to tell\n setup.py not to use `setup.cfg`.\n For example, `USE_SETUPCFG=0 HDF5_INCDIR=/usr/include/hdf5/serial\n HDF5_LIBDIR=/usr/lib/x86_64-linux-gnu/hdf5/serial pip install` has been\n shown to work on an Ubuntu/Debian linux system. Similarly, environment variables\n (all capitalized) can be used to set the include and library paths for\n `hdf5`, `netCDF4`, `hdf4`, `szip`, `jpeg`, `curl` and `zlib`. If the\n libraries are installed in standard places (e.g. `/usr` or `/usr/local`),\n the environment variables do not need to be set.\n - run the tests in the \'test\' directory by running `python run_all.py`.\n\nTutorial\n========\n\n1. [Creating/Opening/Closing a netCDF file.](#section1)\n2. [Groups in a netCDF file.](#section2)\n3. [Dimensions in a netCDF file.](#section3)\n4. [Variables in a netCDF file.](#section4)\n5. [Attributes in a netCDF file.](#section5)\n6. [Writing data to and retrieving data from a netCDF variable.](#section6)\n7. [Dealing with time coordinates.](#section7)\n8. [Reading data from a multi-file netCDF dataset.](#section8)\n9. [Efficient compression of netCDF variables.](#section9)\n10. [Beyond homogeneous arrays of a fixed type - compound data types.](#section10)\n11. [Variable-length (vlen) data types.](#section11)\n12. [Enum data type.](#section12)\n13. [Parallel IO.](#section13)\n14. [Dealing with strings](#section14)\n\n\n## <div id=\'section1\'>1) Creating/Opening/Closing a netCDF file.\n\nTo create a netCDF file from python, you simply call the `netCDF4.Dataset`\nconstructor. This is also the method used to open an existing netCDF\nfile.  If the file is open for write access (`mode=\'w\', \'r+\'` or `\'a\'`), you may\nwrite any type of data including new dimensions, groups, variables and\nattributes.  netCDF files come in five flavors (`NETCDF3_CLASSIC,\nNETCDF3_64BIT_OFFSET, NETCDF3_64BIT_DATA, NETCDF4_CLASSIC`, and `NETCDF4`). \n`NETCDF3_CLASSIC` was the original netcdf binary format, and was limited \nto file sizes less than 2 Gb. `NETCDF3_64BIT_OFFSET` was introduced\nin version 3.6.0 of the library, and extended the original binary format\nto allow for file sizes greater than 2 Gb. \n`NETCDF3_64BIT_DATA` is a new format that requires version 4.4.0 of\nthe C library - it extends the `NETCDF3_64BIT_OFFSET` binary format to\nallow for unsigned/64 bit integer data types and 64-bit dimension sizes.\n`NETCDF3_64BIT` is an alias for `NETCDF3_64BIT_OFFSET`.\n`NETCDF4_CLASSIC` files use the version 4 disk format (HDF5), but omits features\nnot found in the version 3 API. They can be read by netCDF 3 clients\nonly if they have been relinked against the netCDF 4 library. They can\nalso be read by HDF5 clients. `NETCDF4` files use the version 4 disk\nformat (HDF5) and use the new features of the version 4 API.  The\n`netCDF4` module can read and write files in any of these formats. When\ncreating a new file, the format may be specified using the `format`\nkeyword in the `Dataset` constructor.  The default format is\n`NETCDF4`. To see how a given file is formatted, you can examine the\n`data_model` attribute.  Closing the netCDF file is\naccomplished via the `netCDF4.Dataset.close` method of the `netCDF4.Dataset`\ninstance.\n\nHere\'s an example:\n\n    :::python\n    >>> from netCDF4 import Dataset\n    >>> rootgrp = Dataset("test.nc", "w", format="NETCDF4")\n    >>> print rootgrp.data_model\n    NETCDF4\n    >>> rootgrp.close()\n\nRemote [OPeNDAP](http://opendap.org)-hosted datasets can be accessed for\nreading over http if a URL is provided to the `netCDF4.Dataset` constructor instead of a\nfilename.  However, this requires that the netCDF library be built with\nOPenDAP support, via the `--enable-dap` configure option (added in\nversion 4.0.1).\n\n\n## <div id=\'section2\'>2) Groups in a netCDF file.\n\nnetCDF version 4 added support for organizing data in hierarchical\ngroups, which are analogous to directories in a filesystem. Groups serve\nas containers for variables, dimensions and attributes, as well as other\ngroups.  A `netCDF4.Dataset` creates a special group, called\nthe \'root group\', which is similar to the root directory in a unix\nfilesystem.  To create `netCDF4.Group` instances, use the\n`netCDF4.Dataset.createGroup` method of a `netCDF4.Dataset` or `netCDF4.Group`\ninstance. `netCDF4.Dataset.createGroup` takes a single argument, a\npython string containing the name of the new group. The new `netCDF4.Group`\ninstances contained within the root group can be accessed by name using\nthe `groups` dictionary attribute of the `netCDF4.Dataset` instance.  Only\n`NETCDF4` formatted files support Groups, if you try to create a Group\nin a netCDF 3 file you will get an error message.\n\n    :::python\n    >>> rootgrp = Dataset("test.nc", "a")\n    >>> fcstgrp = rootgrp.createGroup("forecasts")\n    >>> analgrp = rootgrp.createGroup("analyses")\n    >>> print rootgrp.groups\n    OrderedDict([("forecasts", \n                  <netCDF4._netCDF4.Group object at 0x1b4b7b0>),\n                 ("analyses", \n                  <netCDF4._netCDF4.Group object at 0x1b4b970>)])\n\nGroups can exist within groups in a `netCDF4.Dataset`, just as directories\nexist within directories in a unix filesystem. Each `netCDF4.Group` instance\nhas a `groups` attribute dictionary containing all of the group\ninstances contained within that group. Each `netCDF4.Group` instance also has a\n`path` attribute that contains a simulated unix directory path to\nthat group.  To simplify the creation of nested groups, you can\nuse a unix-like path as an argument to `netCDF4.Dataset.createGroup`.\n\n    :::python\n    >>> fcstgrp1 = rootgrp.createGroup("/forecasts/model1")\n    >>> fcstgrp2 = rootgrp.createGroup("/forecasts/model2")\n\nIf any of the intermediate elements of the path do not exist, they are created,\njust as with the unix command `\'mkdir -p\'`. If you try to create a group\nthat already exists, no error will be raised, and the existing group will be \nreturned.\n\nHere\'s an example that shows how to navigate all the groups in a\n`netCDF4.Dataset`. The function `walktree` is a Python generator that is used\nto walk the directory tree. Note that printing the `netCDF4.Dataset` or `netCDF4.Group`\nobject yields summary information about it\'s contents.\n\n    :::python\n    >>> def walktree(top):\n    >>>     values = top.groups.values()\n    >>>     yield values\n    >>>     for value in top.groups.values():\n    >>>         for children in walktree(value):\n    >>>             yield children\n    >>> print rootgrp\n    >>> for children in walktree(rootgrp):\n    >>>      for child in children:\n    >>>          print child\n    <type "netCDF4._netCDF4.Dataset">\n    root group (NETCDF4 file format):\n        dimensions:\n        variables:\n        groups: forecasts, analyses\n    <type "netCDF4._netCDF4.Group">\n    group /forecasts:\n        dimensions:\n        variables:\n        groups: model1, model2\n    <type "netCDF4._netCDF4.Group">\n    group /analyses:\n        dimensions:\n        variables:\n        groups:\n    <type "netCDF4._netCDF4.Group">\n    group /forecasts/model1:\n        dimensions:\n        variables:\n        groups:\n    <type "netCDF4._netCDF4.Group">\n    group /forecasts/model2:\n        dimensions:\n        variables:\n        groups:\n\n## <div id=\'section3\'>3) Dimensions in a netCDF file.\n\nnetCDF defines the sizes of all variables in terms of dimensions, so\nbefore any variables can be created the dimensions they use must be\ncreated first. A special case, not often used in practice, is that of a\nscalar variable, which has no dimensions. A dimension is created using\nthe `netCDF4.Dataset.createDimension` method of a `netCDF4.Dataset`\nor `netCDF4.Group` instance. A Python string is used to set the name of the\ndimension, and an integer value is used to set the size. To create an\nunlimited dimension (a dimension that can be appended to), the size\nvalue is set to `None` or 0. In this example, there both the `time` and\n`level` dimensions are unlimited.  Having more than one unlimited\ndimension is a new netCDF 4 feature, in netCDF 3 files there may be only\none, and it must be the first (leftmost) dimension of the variable.\n\n    :::python\n    >>> level = rootgrp.createDimension("level", None)\n    >>> time = rootgrp.createDimension("time", None)\n    >>> lat = rootgrp.createDimension("lat", 73)\n    >>> lon = rootgrp.createDimension("lon", 144)\n\n\nAll of the `netCDF4.Dimension` instances are stored in a python dictionary.\n\n    :::python\n    >>> print rootgrp.dimensions\n    OrderedDict([("level", <netCDF4._netCDF4.Dimension object at 0x1b48030>),\n                 ("time", <netCDF4._netCDF4.Dimension object at 0x1b481c0>),\n                 ("lat", <netCDF4._netCDF4.Dimension object at 0x1b480f8>),\n                 ("lon", <netCDF4._netCDF4.Dimension object at 0x1b48a08>)])\n\nCalling the python `len` function with a `netCDF4.Dimension` instance returns\nthe current size of that dimension.\nThe `netCDF4.Dimension.isunlimited` method of a `netCDF4.Dimension` instance\ncan be used to determine if the dimensions is unlimited, or appendable.\n\n    :::python\n    >>> print len(lon)\n    144\n    >>> print lon.isunlimited()\n    False\n    >>> print time.isunlimited()\n    True\n\nPrinting the `netCDF4.Dimension` object\nprovides useful summary info, including the name and length of the dimension,\nand whether it is unlimited.\n\n    :::python\n    >>> for dimobj in rootgrp.dimensions.values():\n    >>>    print dimobj\n    <type "netCDF4._netCDF4.Dimension"> (unlimited): name = "level", size = 0\n    <type "netCDF4._netCDF4.Dimension"> (unlimited): name = "time", size = 0\n    <type "netCDF4._netCDF4.Dimension">: name = "lat", size = 73\n    <type "netCDF4._netCDF4.Dimension">: name = "lon", size = 144\n    <type "netCDF4._netCDF4.Dimension"> (unlimited): name = "time", size = 0\n\n`netCDF4.Dimension` names can be changed using the\n`netCDF4.Datatset.renameDimension` method of a `netCDF4.Dataset` or\n`netCDF4.Group` instance.\n\n## <div id=\'section4\'>4) Variables in a netCDF file.\n\nnetCDF variables behave much like python multidimensional array objects\nsupplied by the [numpy module](http://numpy.scipy.org). However,\nunlike numpy arrays, netCDF4 variables can be appended to along one or\nmore \'unlimited\' dimensions. To create a netCDF variable, use the\n`netCDF4.Dataset.createVariable` method of a `netCDF4.Dataset` or\n`netCDF4.Group` instance. The `netCDF4.Dataset.createVariable` method\nhas two mandatory arguments, the variable name (a Python string), and\nthe variable datatype. The variable\'s dimensions are given by a tuple\ncontaining the dimension names (defined previously with\n`netCDF4.Dataset.createDimension`). To create a scalar\nvariable, simply leave out the dimensions keyword. The variable\nprimitive datatypes correspond to the dtype attribute of a numpy array.\nYou can specify the datatype as a numpy dtype object, or anything that\ncan be converted to a numpy dtype object.  Valid datatype specifiers\ninclude: `\'f4\'` (32-bit floating point), `\'f8\'` (64-bit floating\npoint), `\'i4\'` (32-bit signed integer), `\'i2\'` (16-bit signed\ninteger), `\'i8\'` (64-bit signed integer), `\'i1\'` (8-bit signed\ninteger), `\'u1\'` (8-bit unsigned integer), `\'u2\'` (16-bit unsigned\ninteger), `\'u4\'` (32-bit unsigned integer), `\'u8\'` (64-bit unsigned\ninteger), or `\'S1\'` (single-character string).  The old Numeric\nsingle-character typecodes (`\'f\'`,`\'d\'`,`\'h\'`,\n`\'s\'`,`\'b\'`,`\'B\'`,`\'c\'`,`\'i\'`,`\'l\'`), corresponding to\n(`\'f4\'`,`\'f8\'`,`\'i2\'`,`\'i2\'`,`\'i1\'`,`\'i1\'`,`\'S1\'`,`\'i4\'`,`\'i4\'`),\nwill also work. The unsigned integer types and the 64-bit integer type\ncan only be used if the file format is `NETCDF4`.\n\nThe dimensions themselves are usually also defined as variables, called\ncoordinate variables. The `netCDF4.Dataset.createVariable`\nmethod returns an instance of the `netCDF4.Variable` class whose methods can be\nused later to access and set variable data and attributes.\n\n    :::python\n    >>> times = rootgrp.createVariable("time","f8",("time",))\n    >>> levels = rootgrp.createVariable("level","i4",("level",))\n    >>> latitudes = rootgrp.createVariable("lat","f4",("lat",))\n    >>> longitudes = rootgrp.createVariable("lon","f4",("lon",))\n    >>> # two dimensions unlimited\n    >>> temp = rootgrp.createVariable("temp","f4",("time","level","lat","lon",))\n\nTo get summary info on a `netCDF4.Variable` instance in an interactive session, just print it.\n\n    :::python\n    >>> print temp\n    <type "netCDF4._netCDF4.Variable">\n    float32 temp(time, level, lat, lon)\n        least_significant_digit: 3\n        units: K\n    unlimited dimensions: time, level\n    current shape = (0, 0, 73, 144)\n\nYou can use a path to create a Variable inside a hierarchy of groups.\n\n    :::python\n    >>> ftemp = rootgrp.createVariable("/forecasts/model1/temp","f4",("time","level","lat","lon",))\n\nIf the intermediate groups do not yet exist, they will be created.\n\nYou can also query a `netCDF4.Dataset` or `netCDF4.Group` instance directly to obtain `netCDF4.Group` or \n`netCDF4.Variable` instances using paths.\n\n    :::python\n    >>> print rootgrp["/forecasts/model1"] # a Group instance\n    <type "netCDF4._netCDF4.Group">\n    group /forecasts/model1:\n        dimensions(sizes):\n        variables(dimensions): float32 temp(time,level,lat,lon)\n        groups:\n    >>> print rootgrp["/forecasts/model1/temp"] # a Variable instance\n    <type "netCDF4._netCDF4.Variable">\n    float32 temp(time, level, lat, lon)\n    path = /forecasts/model1\n    unlimited dimensions: time, level\n    current shape = (0, 0, 73, 144)\n    filling on, default _FillValue of 9.96920996839e+36 used\n\nAll of the variables in the `netCDF4.Dataset` or `netCDF4.Group` are stored in a\nPython dictionary, in the same way as the dimensions:\n\n    :::python\n    >>> print rootgrp.variables\n    OrderedDict([("time", <netCDF4.Variable object at 0x1b4ba70>),\n                 ("level", <netCDF4.Variable object at 0x1b4bab0>),\n                 ("lat", <netCDF4.Variable object at 0x1b4baf0>),\n                 ("lon", <netCDF4.Variable object at 0x1b4bb30>),\n                 ("temp", <netCDF4.Variable object at 0x1b4bb70>)])\n\n`netCDF4.Variable` names can be changed using the\n`netCDF4.Dataset.renameVariable` method of a `netCDF4.Dataset`\ninstance.\n\n\n## <div id=\'section5\'>5) Attributes in a netCDF file.\n\nThere are two types of attributes in a netCDF file, global and variable.\nGlobal attributes provide information about a group, or the entire\ndataset, as a whole. `netCDF4.Variable` attributes provide information about\none of the variables in a group. Global attributes are set by assigning\nvalues to `netCDF4.Dataset` or `netCDF4.Group` instance variables. `netCDF4.Variable`\nattributes are set by assigning values to `netCDF4.Variable` instances\nvariables. Attributes can be strings, numbers or sequences. Returning to\nour example,\n\n    :::python\n    >>> import time\n    >>> rootgrp.description = "bogus example script"\n    >>> rootgrp.history = "Created " + time.ctime(time.time())\n    >>> rootgrp.source = "netCDF4 python module tutorial"\n    >>> latitudes.units = "degrees north"\n    >>> longitudes.units = "degrees east"\n    >>> levels.units = "hPa"\n    >>> temp.units = "K"\n    >>> times.units = "hours since 0001-01-01 00:00:00.0"\n    >>> times.calendar = "gregorian"\n\nThe `netCDF4.Dataset.ncattrs` method of a `netCDF4.Dataset`, `netCDF4.Group` or\n`netCDF4.Variable` instance can be used to retrieve the names of all the netCDF\nattributes. This method is provided as a convenience, since using the\nbuilt-in `dir` Python function will return a bunch of private methods\nand attributes that cannot (or should not) be modified by the user.\n\n    :::python\n    >>> for name in rootgrp.ncattrs():\n    >>>     print "Global attr", name, "=", getattr(rootgrp,name)\n    Global attr description = bogus example script\n    Global attr history = Created Mon Nov  7 10.30:56 2005\n    Global attr source = netCDF4 python module tutorial\n\nThe `__dict__` attribute of a `netCDF4.Dataset`, `netCDF4.Group` or `netCDF4.Variable`\ninstance provides all the netCDF attribute name/value pairs in a python\ndictionary:\n\n    :::python\n    >>> print rootgrp.__dict__\n    OrderedDict([(u"description", u"bogus example script"),\n                 (u"history", u"Created Thu Mar  3 19:30:33 2011"),\n                 (u"source", u"netCDF4 python module tutorial")])\n\nAttributes can be deleted from a netCDF `netCDF4.Dataset`, `netCDF4.Group` or\n`netCDF4.Variable` using the python `del` statement (i.e. `del grp.foo`\nremoves the attribute `foo` the the group `grp`).\n\n## <div id=\'section6\'>6) Writing data to and retrieving data from a netCDF variable.\n\nNow that you have a netCDF `netCDF4.Variable` instance, how do you put data\ninto it? You can just treat it like an array and assign data to a slice.\n\n    :::python\n    >>> import numpy\n    >>> lats =  numpy.arange(-90,91,2.5)\n    >>> lons =  numpy.arange(-180,180,2.5)\n    >>> latitudes[:] = lats\n    >>> longitudes[:] = lons\n    >>> print "latitudes =\\n",latitudes[:]\n    latitudes =\n    [-90.  -87.5 -85.  -82.5 -80.  -77.5 -75.  -72.5 -70.  -67.5 -65.  -62.5\n     -60.  -57.5 -55.  -52.5 -50.  -47.5 -45.  -42.5 -40.  -37.5 -35.  -32.5\n     -30.  -27.5 -25.  -22.5 -20.  -17.5 -15.  -12.5 -10.   -7.5  -5.   -2.5\n       0.    2.5   5.    7.5  10.   12.5  15.   17.5  20.   22.5  25.   27.5\n      30.   32.5  35.   37.5  40.   42.5  45.   47.5  50.   52.5  55.   57.5\n      60.   62.5  65.   67.5  70.   72.5  75.   77.5  80.   82.5  85.   87.5\n      90. ]\n\nUnlike NumPy\'s array objects, netCDF `netCDF4.Variable`\nobjects with unlimited dimensions will grow along those dimensions if you\nassign data outside the currently defined range of indices.\n\n    :::python\n    >>> # append along two unlimited dimensions by assigning to slice.\n    >>> nlats = len(rootgrp.dimensions["lat"])\n    >>> nlons = len(rootgrp.dimensions["lon"])\n    >>> print "temp shape before adding data = ",temp.shape\n    temp shape before adding data =  (0, 0, 73, 144)\n    >>>\n    >>> from numpy.random import uniform\n    >>> temp[0:5,0:10,:,:] = uniform(size=(5,10,nlats,nlons))\n    >>> print "temp shape after adding data = ",temp.shape\n    temp shape after adding data =  (6, 10, 73, 144)\n    >>>\n    >>> # levels have grown, but no values yet assigned.\n    >>> print "levels shape after adding pressure data = ",levels.shape\n    levels shape after adding pressure data =  (10,)\n\nNote that the size of the levels variable grows when data is appended\nalong the `level` dimension of the variable `temp`, even though no\ndata has yet been assigned to levels.\n\n    :::python\n    >>> # now, assign data to levels dimension variable.\n    >>> levels[:] =  [1000.,850.,700.,500.,300.,250.,200.,150.,100.,50.]\n\nHowever, that there are some differences between NumPy and netCDF\nvariable slicing rules. Slices behave as usual, being specified as a\n`start:stop:step` triplet. Using a scalar integer index `i` takes the ith\nelement and reduces the rank of the output array by one. Boolean array and\ninteger sequence indexing behaves differently for netCDF variables\nthan for numpy arrays.  Only 1-d boolean arrays and integer sequences are\nallowed, and these indices work independently along each dimension (similar\nto the way vector subscripts work in fortran).  This means that\n\n    :::python\n    >>> temp[0, 0, [0,1,2,3], [0,1,2,3]]\n\nreturns an array of shape (4,4) when slicing a netCDF variable, but for a\nnumpy array it returns an array of shape (4,).\nSimilarly, a netCDF variable of shape `(2,3,4,5)` indexed\nwith `[0, array([True, False, True]), array([False, True, True, True]), :]`\nwould return a `(2, 3, 5)` array. In NumPy, this would raise an error since\nit would be equivalent to `[0, [0,1], [1,2,3], :]`. When slicing with integer\nsequences, the indices ***need not be sorted*** and ***may contain\nduplicates*** (both of these are new features in version 1.2.1).\nWhile this behaviour may cause some confusion for those used to NumPy\'s \'fancy indexing\' rules,\nit provides a very powerful way to extract data from multidimensional netCDF\nvariables by using logical operations on the dimension arrays to create slices.\n\nFor example,\n\n    :::python\n    >>> tempdat = temp[::2, [1,3,6], lats>0, lons>0]\n\nwill extract time indices 0,2 and 4, pressure levels\n850, 500 and 200 hPa, all Northern Hemisphere latitudes and Eastern\nHemisphere longitudes, resulting in a numpy array of shape  (3, 3, 36, 71).\n\n    :::python\n    >>> print "shape of fancy temp slice = ",tempdat.shape\n    shape of fancy temp slice =  (3, 3, 36, 71)\n\n***Special note for scalar variables***: To extract data from a scalar variable\n`v` with no associated dimensions, use `numpy.asarray(v)` or `v[...]`. The result\nwill be a numpy scalar array.\n\nBy default, netcdf4-python returns numpy masked arrays with values equal to the\n`missing_value` or `_FillValue` variable attributes masked.  The\n`netCDF4.Dataset.set_auto_mask`  `netCDF4.Dataset` and `netCDF4.Variable` methods\ncan be used to disable this feature so that\nnumpy arrays are always returned, with the missing values included. Prior to\nversion 1.4.0 the default behavior was to only return masked arrays when the\nrequested slice contained missing values.  This behavior can be recovered\nusing the `netCDF4.Dataset.set_always_mask` method. If a masked array is\nwritten to a netCDF variable, the masked elements are filled with the\nvalue specified by the `missing_value` attribute.  If the variable has\nno `missing_value`, the `_FillValue` is used instead.\n\n## <div id=\'section7\'>7) Dealing with time coordinates.\n\nTime coordinate values pose a special challenge to netCDF users.  Most\nmetadata standards (such as CF) specify that time should be\nmeasure relative to a fixed date using a certain calendar, with units\nspecified like `hours since YY-MM-DD hh:mm:ss`.  These units can be\nawkward to deal with, without a utility to convert the values to and\nfrom calendar dates.  The function called `netCDF4.num2date` and `netCDF4.date2num` are\nprovided with this package to do just that (starting with version 1.4.0, the \n[cftime](https://unidata.github.io/cftime) package must be installed\nseparately).  Here\'s an example of how they\ncan be used:\n\n    :::python\n    >>> # fill in times.\n    >>> from datetime import datetime, timedelta\n    >>> from netCDF4 import num2date, date2num\n    >>> dates = [datetime(2001,3,1)+n*timedelta(hours=12) for n in range(temp.shape[0])]\n    >>> times[:] = date2num(dates,units=times.units,calendar=times.calendar)\n    >>> print "time values (in units %s): " % times.units+"\\n",times[:]\n    time values (in units hours since January 1, 0001):\n    [ 17533056.  17533068.  17533080.  17533092.  17533104.]\n    >>> dates = num2date(times[:],units=times.units,calendar=times.calendar)\n    >>> print "dates corresponding to time values:\\n",dates\n    dates corresponding to time values:\n    [2001-03-01 00:00:00 2001-03-01 12:00:00 2001-03-02 00:00:00\n     2001-03-02 12:00:00 2001-03-03 00:00:00]\n\n`netCDF4.num2date` converts numeric values of time in the specified `units`\nand `calendar` to datetime objects, and `netCDF4.date2num` does the reverse.\nAll the calendars currently defined in the\n[CF metadata convention](http://cfconventions.org) are supported.\nA function called `netCDF4.date2index` is also provided which returns the indices\nof a netCDF time variable corresponding to a sequence of datetime instances.\n\n\n## <div id=\'section8\'>8) Reading data from a multi-file netCDF dataset.\n\nIf you want to read data from a variable that spans multiple netCDF files,\nyou can use the `netCDF4.MFDataset` class to read the data as if it were\ncontained in a single file. Instead of using a single filename to create\na `netCDF4.Dataset` instance, create a `netCDF4.MFDataset` instance with either a list\nof filenames, or a string with a wildcard (which is then converted to\na sorted list of files using the python glob module).\nVariables in the list of files that share the same unlimited\ndimension are aggregated together, and can be sliced across multiple\nfiles.  To illustrate this, let\'s first create a bunch of netCDF files with\nthe same variable (with the same unlimited dimension).  The files\nmust in be in `NETCDF3_64BIT_OFFSET`, `NETCDF3_64BIT_DATA`, `NETCDF3_CLASSIC` or\n`NETCDF4_CLASSIC` format (`NETCDF4` formatted multi-file\ndatasets are not supported).\n\n    :::python\n    >>> for nf in range(10):\n    >>>     f = Dataset("mftest%s.nc" % nf,"w")\n    >>>     f.createDimension("x",None)\n    >>>     x = f.createVariable("x","i",("x",))\n    >>>     x[0:10] = numpy.arange(nf*10,10*(nf+1))\n    >>>     f.close()\n\nNow read all the files back in at once with `netCDF4.MFDataset`\n\n    :::python\n    >>> from netCDF4 import MFDataset\n    >>> f = MFDataset("mftest*nc")\n    >>> print f.variables["x"][:]\n    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24\n     25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49\n     50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74\n     75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]\n\nNote that `netCDF4.MFDataset` can only be used to read, not write, multi-file\ndatasets.\n\n## <div id=\'section9\'>9) Efficient compression of netCDF variables.\n\nData stored in netCDF 4 `netCDF4.Variable` objects can be compressed and\ndecompressed on the fly. The parameters for the compression are\ndetermined by the `zlib`, `complevel` and `shuffle` keyword arguments\nto the `netCDF4.Dataset.createVariable` method. To turn on\ncompression, set `zlib=True`.  The `complevel` keyword regulates the\nspeed and efficiency of the compression (1 being fastest, but lowest\ncompression ratio, 9 being slowest but best compression ratio). The\ndefault value of `complevel` is 4. Setting `shuffle=False` will turn\noff the HDF5 shuffle filter, which de-interlaces a block of data before\ncompression by reordering the bytes.  The shuffle filter can\nsignificantly improve compression ratios, and is on by default.  Setting\n`fletcher32` keyword argument to\n`netCDF4.Dataset.createVariable` to `True` (it\'s `False` by\ndefault) enables the Fletcher32 checksum algorithm for error detection.\nIt\'s also possible to set the HDF5 chunking parameters and endian-ness\nof the binary data stored in the HDF5 file with the `chunksizes`\nand `endian` keyword arguments to\n`netCDF4.Dataset.createVariable`.  These keyword arguments only\nare relevant for `NETCDF4` and `NETCDF4_CLASSIC` files (where the\nunderlying file format is HDF5) and are silently ignored if the file\nformat is `NETCDF3_CLASSIC`, `NETCDF3_64BIT_OFFSET` or `NETCDF3_64BIT_DATA`.\n\nIf your data only has a certain number of digits of precision (say for\nexample, it is temperature data that was measured with a precision of\n0.1 degrees), you can dramatically improve zlib compression by\nquantizing (or truncating) the data using the `least_significant_digit`\nkeyword argument to `netCDF4.Dataset.createVariable`. The least\nsignificant digit is the power of ten of the smallest decimal place in\nthe data that is a reliable value. For example if the data has a\nprecision of 0.1, then setting `least_significant_digit=1` will cause\ndata the data to be quantized using `numpy.around(scale*data)/scale`, where\nscale = 2**bits, and bits is determined so that a precision of 0.1 is\nretained (in this case bits=4).  Effectively, this makes the compression\n\'lossy\' instead of \'lossless\', that is some precision in the data is\nsacrificed for the sake of disk space.\n\nIn our example, try replacing the line\n\n    :::python\n    >>> temp = rootgrp.createVariable("temp","f4",("time","level","lat","lon",))\n\nwith\n\n    :::python\n    >>> temp = dataset.createVariable("temp","f4",("time","level","lat","lon",),zlib=True)\n\nand then\n\n    :::python\n    >>> temp = dataset.createVariable("temp","f4",("time","level","lat","lon",),zlib=True,least_significant_digit=3)\n\nand see how much smaller the resulting files are.\n\n## <div id=\'section10\'>10) Beyond homogeneous arrays of a fixed type - compound data types.\n\nCompound data types map directly to numpy structured (a.k.a \'record\')\narrays.  Structured arrays are akin to C structs, or derived types\nin Fortran. They allow for the construction of table-like structures\ncomposed of combinations of other data types, including other\ncompound types. Compound types might be useful for representing multiple\nparameter values at each point on a grid, or at each time and space\nlocation for scattered (point) data. You can then access all the\ninformation for a point by reading one variable, instead of reading\ndifferent parameters from different variables.  Compound data types\nare created from the corresponding numpy data type using the\n`netCDF4.Dataset.createCompoundType` method of a `netCDF4.Dataset` or `netCDF4.Group` instance.\nSince there is no native complex data type in netcdf, compound types are handy\nfor storing numpy complex arrays.  Here\'s an example:\n\n    :::python\n    >>> f = Dataset("complex.nc","w")\n    >>> size = 3 # length of 1-d complex array\n    >>> # create sample complex data.\n    >>> datac = numpy.exp(1j*(1.+numpy.linspace(0, numpy.pi, size)))\n    >>> # create complex128 compound data type.\n    >>> complex128 = numpy.dtype([("real",numpy.float64),("imag",numpy.float64)])\n    >>> complex128_t = f.createCompoundType(complex128,"complex128")\n    >>> # create a variable with this data type, write some data to it.\n    >>> f.createDimension("x_dim",None)\n    >>> v = f.createVariable("cmplx_var",complex128_t,"x_dim")\n    >>> data = numpy.empty(size,complex128) # numpy structured array\n    >>> data["real"] = datac.real; data["imag"] = datac.imag\n    >>> v[:] = data # write numpy structured array to netcdf compound var\n    >>> # close and reopen the file, check the contents.\n    >>> f.close(); f = Dataset("complex.nc")\n    >>> v = f.variables["cmplx_var"]\n    >>> datain = v[:] # read in all the data into a numpy structured array\n    >>> # create an empty numpy complex array\n    >>> datac2 = numpy.empty(datain.shape,numpy.complex128)\n    >>> # .. fill it with contents of structured array.\n    >>> datac2.real = datain["real"]; datac2.imag = datain["imag"]\n    >>> print datac.dtype,datac # original data\n    complex128 [ 0.54030231+0.84147098j -0.84147098+0.54030231j  -0.54030231-0.84147098j]\n    >>>\n    >>> print datac2.dtype,datac2 # data from file\n    complex128 [ 0.54030231+0.84147098j -0.84147098+0.54030231j  -0.54030231-0.84147098j]\n\nCompound types can be nested, but you must create the \'inner\'\nones first. All possible numpy structured arrays cannot be\nrepresented as Compound variables - an error message will be\nraise if you try to create one that is not supported.\nAll of the compound types defined for a `netCDF4.Dataset` or `netCDF4.Group` are stored \nin a Python dictionary, just like variables and dimensions. As always, printing\nobjects gives useful summary information in an interactive session:\n\n    :::python\n    >>> print f\n    <type "netCDF4._netCDF4.Dataset">\n    root group (NETCDF4 file format):\n        dimensions: x_dim\n        variables: cmplx_var\n        groups:\n    <type "netCDF4._netCDF4.Variable">\n    >>> print f.variables["cmplx_var"]\n    compound cmplx_var(x_dim)\n    compound data type: [("real", "<f8"), ("imag", "<f8")]\n    unlimited dimensions: x_dim\n    current shape = (3,)\n    >>> print f.cmptypes\n    OrderedDict([("complex128", <netCDF4.CompoundType object at 0x1029eb7e8>)])\n    >>> print f.cmptypes["complex128"]\n    <type "netCDF4._netCDF4.CompoundType">: name = "complex128", numpy dtype = [(u"real","<f8"), (u"imag", "<f8")]\n\n## <div id=\'section11\'>11) Variable-length (vlen) data types.\n\nNetCDF 4 has support for variable-length or "ragged" arrays.  These are arrays\nof variable length sequences having the same type. To create a variable-length\ndata type, use the `netCDF4.Dataset.createVLType` method\nmethod of a `netCDF4.Dataset` or `netCDF4.Group` instance.\n\n    :::python\n    >>> f = Dataset("tst_vlen.nc","w")\n    >>> vlen_t = f.createVLType(numpy.int32, "phony_vlen")\n\nThe numpy datatype of the variable-length sequences and the name of the\nnew datatype must be specified. Any of the primitive datatypes can be\nused (signed and unsigned integers, 32 and 64 bit floats, and characters),\nbut compound data types cannot.\nA new variable can then be created using this datatype.\n\n    :::python\n    >>> x = f.createDimension("x",3)\n    >>> y = f.createDimension("y",4)\n    >>> vlvar = f.createVariable("phony_vlen_var", vlen_t, ("y","x"))\n\nSince there is no native vlen datatype in numpy, vlen arrays are represented\nin python as object arrays (arrays of dtype `object`). These are arrays whose\nelements are Python object pointers, and can contain any type of python object.\nFor this application, they must contain 1-D numpy arrays all of the same type\nbut of varying length.\nIn this case, they contain 1-D numpy `int32` arrays of random length between\n1 and 10.\n\n    :::python\n    >>> import random\n    >>> data = numpy.empty(len(y)*len(x),object)\n    >>> for n in range(len(y)*len(x)):\n    >>>    data[n] = numpy.arange(random.randint(1,10),dtype="int32")+1\n    >>> data = numpy.reshape(data,(len(y),len(x)))\n    >>> vlvar[:] = data\n    >>> print "vlen variable =\\n",vlvar[:]\n    vlen variable =\n    [[[ 1  2  3  4  5  6  7  8  9 10] [1 2 3 4 5] [1 2 3 4 5 6 7 8]]\n     [[1 2 3 4 5 6 7] [1 2 3 4 5 6] [1 2 3 4 5]]\n     [[1 2 3 4 5] [1 2 3 4] [1]]\n     [[ 1  2  3  4  5  6  7  8  9 10] [ 1  2  3  4  5  6  7  8  9 10]\n      [1 2 3 4 5 6 7 8]]]\n    >>> print f\n    <type "netCDF4._netCDF4.Dataset">\n    root group (NETCDF4 file format):\n        dimensions: x, y\n        variables: phony_vlen_var\n        groups:\n    >>> print f.variables["phony_vlen_var"]\n    <type "netCDF4._netCDF4.Variable">\n    vlen phony_vlen_var(y, x)\n    vlen data type: int32\n    unlimited dimensions:\n    current shape = (4, 3)\n    >>> print f.VLtypes["phony_vlen"]\n    <type "netCDF4._netCDF4.VLType">: name = "phony_vlen", numpy dtype = int32\n\nNumpy object arrays containing python strings can also be written as vlen\nvariables,  For vlen strings, you don\'t need to create a vlen data type.\nInstead, simply use the python `str` builtin (or a numpy string datatype\nwith fixed length greater than 1) when calling the\n`netCDF4.Dataset.createVariable` method.\n\n    :::python\n    >>> z = f.createDimension("z",10)\n    >>> strvar = rootgrp.createVariable("strvar", str, "z")\n\nIn this example, an object array is filled with random python strings with\nrandom lengths between 2 and 12 characters, and the data in the object\narray is assigned to the vlen string variable.\n\n    :::python\n    >>> chars = "1234567890aabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"\n    >>> data = numpy.empty(10,"O")\n    >>> for n in range(10):\n    >>>     stringlen = random.randint(2,12)\n    >>>     data[n] = "".join([random.choice(chars) for i in range(stringlen)])\n    >>> strvar[:] = data\n    >>> print "variable-length string variable:\\n",strvar[:]\n    variable-length string variable:\n    [aDy29jPt 5DS9X8 jd7aplD b8t4RM jHh8hq KtaPWF9cQj Q1hHN5WoXSiT MMxsVeq tdLUzvVTzj]\n    >>> print f\n    <type "netCDF4._netCDF4.Dataset">\n    root group (NETCDF4 file format):\n        dimensions: x, y, z\n        variables: phony_vlen_var, strvar\n        groups:\n    >>> print f.variables["strvar"]\n    <type "netCDF4._netCDF4.Variable">\n    vlen strvar(z)\n    vlen data type: <type "str">\n    unlimited dimensions:\n    current size = (10,)\n\nIt is also possible to set contents of vlen string variables with numpy arrays\nof any string or unicode data type. Note, however, that accessing the contents\nof such variables will always return numpy arrays with dtype `object`.\n\n## <div id=\'section12\'>12) Enum data type.\n\nnetCDF4 has an enumerated data type, which is an integer datatype that is\nrestricted to certain named values. Since Enums don\'t map directly to\na numpy data type, they are read and written as integer arrays.\n\nHere\'s an example of using an Enum type to hold cloud type data. \nThe base integer data type and a python dictionary describing the allowed\nvalues and their names are used to define an Enum data type using\n`netCDF4.Dataset.createEnumType`.\n\n    :::python\n    >>> nc = Dataset(\'clouds.nc\',\'w\')\n    >>> # python dict with allowed values and their names.\n    >>> enum_dict = {u\'Altocumulus\': 7, u\'Missing\': 255, \n    >>> u\'Stratus\': 2, u\'Clear\': 0,\n    >>> u\'Nimbostratus\': 6, u\'Cumulus\': 4, u\'Altostratus\': 5,\n    >>> u\'Cumulonimbus\': 1, u\'Stratocumulus\': 3}\n    >>> # create the Enum type called \'cloud_t\'.\n    >>> cloud_type = nc.createEnumType(numpy.uint8,\'cloud_t\',enum_dict)\n    >>> print cloud_type\n    <type \'netCDF4._netCDF4.EnumType\'>: name = \'cloud_t\',\n    numpy dtype = uint8, fields/values ={u\'Cumulus\': 4,\n    u\'Altocumulus\': 7, u\'Missing\': 255,\n    u\'Stratus\': 2, u\'Clear\': 0,\n    u\'Cumulonimbus\': 1, u\'Stratocumulus\': 3,\n    u\'Nimbostratus\': 6, u\'Altostratus\': 5}\n\nA new variable can be created in the usual way using this data type.\nInteger data is written to the variable that represents the named\ncloud types in enum_dict. A `ValueError` will be raised if an attempt\nis made to write an integer value not associated with one of the\nspecified names.\n\n    :::python\n    >>> time = nc.createDimension(\'time\',None)\n    >>> # create a 1d variable of type \'cloud_type\'.\n    >>> # The fill_value is set to the \'Missing\' named value.\n    >>> cloud_var =\n    >>> nc.createVariable(\'primary_cloud\',cloud_type,\'time\',\n    >>> fill_value=enum_dict[\'Missing\'])\n    >>> # write some data to the variable.\n    >>> cloud_var[:] = [enum_dict[\'Clear\'],enum_dict[\'Stratus\'],\n    >>> enum_dict[\'Cumulus\'],enum_dict[\'Missing\'],\n    >>> enum_dict[\'Cumulonimbus\']]\n    >>> nc.close()\n    >>> # reopen the file, read the data.\n    >>> nc = Dataset(\'clouds.nc\')\n    >>> cloud_var = nc.variables[\'primary_cloud\']\n    >>> print cloud_var\n    <type \'netCDF4._netCDF4.Variable\'>\n    enum primary_cloud(time)\n        _FillValue: 255\n    enum data type: uint8\n    unlimited dimensions: time\n    current shape = (5,)\n    >>> print cloud_var.datatype.enum_dict\n    {u\'Altocumulus\': 7, u\'Missing\': 255, u\'Stratus\': 2,\n    u\'Clear\': 0, u\'Nimbostratus\': 6, u\'Cumulus\': 4,\n    u\'Altostratus\': 5, u\'Cumulonimbus\': 1,\n    u\'Stratocumulus\': 3}\n    >>> print cloud_var[:]\n    [0 2 4 -- 1]\n    >>> nc.close()\n\n## <div id=\'section13\'>13) Parallel IO.\n\nIf MPI parallel enabled versions of netcdf and hdf5 are detected, and\n[mpi4py](https://mpi4py.scipy.org) is installed, netcdf4-python will\nbe built with parallel IO capabilities enabled.  To use parallel IO,\nyour program must be running in an MPI environment using \n[mpi4py](https://mpi4py.scipy.org).\n\n    :::python\n    >>> from mpi4py import MPI\n    >>> import numpy as np\n    >>> from netCDF4 import Dataset\n    >>> rank = MPI.COMM_WORLD.rank  # The process ID (integer 0-3 for 4-process run)\n\nTo run an MPI-based parallel program like this, you must use `mpiexec` to launch several\nparallel instances of Python (for example, using `mpiexec -np 4 python mpi_example.py`).\nThe parallel features of netcdf4-python are mostly transparent -\nwhen a new dataset is created or an existing dataset is opened,\nuse the `parallel` keyword to enable parallel access.\n\n    :::python\n    >>> nc = Dataset(\'parallel_tst.nc\',\'w\',parallel=True)\n\nThe optional `comm` keyword may be used to specify a particular\nMPI communicator (`MPI_COMM_WORLD` is used by default).  Each process (or rank)\ncan now write to the file indepedently.  In this example the process rank is\nwritten to a different variable index on each task\n\n    :::python\n    >>> d = nc.createDimension(\'dim\',4)\n    >>> v = nc.createVariable(\'var\', numpy.int, \'dim\')\n    >>> v[rank] = rank\n    >>> nc.close()\n\n    % ncdump parallel_test.nc\n    netcdf parallel_test {\n    dimensions:\n        dim = 4 ;\n        variables:\n        int64 var(dim) ;\n        data:\n\n        var = 0, 1, 2, 3 ;\n    }\n\nThere are two types of parallel IO, independent (the default) and collective.\nIndependent IO means that each process can do IO independently. It should not\ndepend on or be affected by other processes. Collective IO is a way of doing\nIO defined in the MPI-IO standard; unlike independent IO, all processes must\nparticipate in doing IO. To toggle back and forth between\nthe two types of IO, use the `netCDF4.Variable.set_collective`\n`netCDF4.Variable`method. All metadata\noperations (such as creation of groups, types, variables, dimensions, or attributes)\nare collective.  There are a couple of important limitatons of parallel IO:\n\n - If a variable has an unlimited dimension, appending data must be done in collective mode.\n   If the write is done in independent mode, the operation will fail with a\n   a generic "HDF Error".\n - You cannot write compressed data in parallel (although\n   you can read it).\n - You cannot use variable-length (VLEN) data types. \n\n## <div id=\'section14\'>14) Dealing with strings.\n\nThe most flexible way to store arrays of strings is with the \n[Variable-length (vlen) string data type](#section11). However, this requires\nthe use of the NETCDF4 data model, and the vlen type does not map very well\nnumpy arrays (you have to use numpy arrays of dtype=`object`, which are arrays of\narbitrary python objects). numpy does have a fixed-width string array\ndata type, but unfortunately the netCDF data model does not.\nInstead fixed-width byte strings are typically stored as [arrays of 8-bit\ncharacters](https://www.unidata.ucar.edu/software/netcdf/docs/BestPractices.html#bp_Strings-and-Variables-of-type-char).\nTo perform the conversion to and from character arrays to fixed-width numpy string arrays, the\nfollowing convention is followed by the python interface.\nIf the `_Encoding` special attribute is set for a character array\n(dtype `S1`) variable, the `netCDF4.chartostring` utility function is used to convert the array of\ncharacters to an array of strings with one less dimension (the last dimension is\ninterpreted as the length of each string) when reading the data. The character\nset (usually ascii) is specified by the `_Encoding` attribute. If `_Encoding`\nis \'none\' or \'bytes\', then the character array is converted to a numpy\nfixed-width byte string array (dtype `S#`), otherwise a numpy unicode (dtype\n`U#`) array is created.  When writing the data,\n`netCDF4.stringtochar` is used to convert the numpy string array to an array of\ncharacters with one more dimension. For example,\n\n    :::python\n    >>> nc = Dataset(\'stringtest.nc\',\'w\',format=\'NETCDF4_CLASSIC\')\n    >>> nc.createDimension(\'nchars\',3)\n    >>> nc.createDimension(\'nstrings\',None)\n    >>> v = nc.createVariable(\'strings\',\'S1\',(\'nstrings\',\'nchars\'))\n    >>> datain = numpy.array([\'foo\',\'bar\'],dtype=\'S3\')\n    >>> v[:] = stringtochar(datain) # manual conversion to char array\n    >>> v[:] # data returned as char array\n    [[b\'f\' b\'o\' b\'o\']\n    [b\'b\' b\'a\' b\'r\']]\n    >>> v._Encoding = \'ascii\' # this enables automatic conversion\n    >>> v[:] = datain # conversion to char array done internally\n    >>> v[:] # data returned in numpy string array\n    [\'foo\' \'bar\']\n    >>> nc.close()\n\nEven if the `_Encoding` attribute is set, the automatic conversion of char\narrays to/from string arrays can be disabled with\n`netCDF4.Variable.set_auto_chartostring`. \n\nA similar situation is often encountered with numpy structured arrays with subdtypes\ncontaining fixed-wdith byte strings (dtype=`S#`). Since there is no native fixed-length string\nnetCDF datatype, these numpy structure arrays are mapped onto netCDF compound\ntypes with character array elements.  In this case the string <-> char array\nconversion is handled automatically (without the need to set the `_Encoding`\nattribute) using [numpy\nviews](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.view.html).\nThe structured array dtype (including the string elements) can even be used to\ndefine the compound data type - the string dtype will be converted to\ncharacter array dtype under the hood when creating the netcdf compound type.\nHere\'s an example:\n\n    :::python\n    >>> nc = Dataset(\'compoundstring_example.nc\',\'w\')\n    >>> dtype = numpy.dtype([(\'observation\', \'f4\'),\n                      (\'station_name\',\'S80\')])\n    >>> station_data_t = nc.createCompoundType(dtype,\'station_data\')\n    >>> nc.createDimension(\'station\',None)\n    >>> statdat = nc.createVariable(\'station_obs\', station_data_t, (\'station\',))\n    >>> data = numpy.empty(2,dtype)\n    >>> data[\'observation\'][:] = (123.,3.14)\n    >>> data[\'station_name\'][:] = (\'Boulder\',\'New York\')\n    >>> statdat.dtype # strings actually stored as character arrays\n    {\'names\':[\'observation\',\'station_name\'], \'formats\':[\'<f4\',(\'S1\', (80,))], \'offsets\':[0,4], \'itemsize\':84, \'aligned\':True}\n    >>> statdat[:] = data # strings converted to character arrays internally\n    >>> statdat[:] # character arrays converted back to strings\n    [(123.  , \'Boulder\') (  3.14, \'New York\')]\n    >>> statdat[:].dtype\n    {\'names\':[\'observation\',\'station_name\'], \'formats\':[\'<f4\',\'S80\'], \'offsets\':[0,4], \'itemsize\':84, \'aligned\':True}\n    >>> statdat.set_auto_chartostring(False) # turn off auto-conversion\n    >>> statdat[:] = data.view(dtype=[(\'observation\', \'f4\'),(\'station_name\',\'S1\',10)])\n    >>> statdat[:] # now structured array with char array subtype is returned\n    [(123.  , [\'B\', \'o\', \'u\', \'l\', \'d\', \'e\', \'r\', \'\', \'\', \'\'])\n    (  3.14, [\'N\', \'e\', \'w\', \' \', \'Y\', \'o\', \'r\', \'k\', \'\', \'\'])]\n    >>> nc.close()\n\nNote that there is currently no support for mapping numpy structured arrays with\nunicode elements (dtype `U#`) onto netCDF compound types, nor is there support \nfor netCDF compound types with vlen string components.\n\nAll of the code in this tutorial is available in `examples/tutorial.py`, except\nthe parallel IO example, which is in `examples/mpi_example.py`.\nUnit tests are in the `test` directory.\n\n**contact**: Jeffrey Whitaker <jeffrey.s.whitaker@noaa.gov>\n\n**copyright**: 2008 by Jeffrey Whitaker.\n\n**license**: Permission to use, copy, modify, and distribute this software and\nits documentation for any purpose and without fee is hereby granted,\nprovided that the above copyright notice appear in all copies and that\nboth the copyright notice and this permission notice appear in\nsupporting documentation.\nTHE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,\nINCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO\nEVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR\nCONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF\nUSE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR\nOTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR\nPERFORMANCE OF THIS SOFTWARE.\n- - -\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/netCDF4/_netCDF4.cpython-36m-x86_64-linux-gnu.so'
__has_cdf5_format__ = 1
__has_nc_inq_format_extended__ = 1
__has_nc_inq_path__ = 1
__has_nc_open_mem__ = 1
__has_nc_par__ = 0
__has_rename_grp__ = 1
__hdf5libversion__ = '1.10.2'
__name__ = 'netCDF4._netCDF4'
__netcdf4libversion__ = '4.6.1'
__package__ = 'netCDF4'
__path__ = None
__pdoc__ = _mod_builtins.dict()
def __pyx_unpickle_Dimension():
    pass

__test__ = _mod_builtins.dict()
__version__ = '1.4.2'
def _find_dim(grp, dimname):
    pass

_format_dict = _mod_builtins.dict()
def _gethdf5libversion():
    pass

_intnptonctype = _mod_builtins.dict()
def _is_int(a):
    pass

_key = 'f8'
_nctonptype = _mod_builtins.dict()
_needsworkaround_issue485 = False
_nptonctype = _mod_builtins.dict()
def _out_array_shape(count):
    'Return the output array shape given the count array created by getStartCountStride'
    pass

_private_atts = _mod_builtins.list()
def _quantize(data, least_significant_digit):
    '\nquantize data to improve compression. data is quantized using\naround(scale*data)/scale, where scale is 2**bits, and bits is determined\nfrom the least_significant_digit. For example, if\nleast_significant_digit=1, bits will be 4.\n    '
    pass

_reverse_format_dict = _mod_builtins.dict()
def _safecast(a, b):
    pass

def _set_alignment():
    pass

def _set_default_format():
    pass

def _set_viewdtype():
    pass

def _sortbylist(A, B):
    pass

_supportedtypes = _mod_builtins.dict_keys()
def _to_ascii():
    pass

def _tostr(s):
    pass

_value = 6
def _walk_grps(topgrp):
    'Iterate through all (sub-) groups of topgrp, similar to os.walktree.\n\n    '
    pass

buffer = _mod_builtins.memoryview
def chartostring():
    "\n**`chartostring(b,encoding='utf-8')`**\n\nconvert a character array to a string array with one less dimension.\n\n**`b`**:  Input character array (numpy datatype `'S1'` or `'U1'`).\nWill be converted to a array of strings, where each string has a fixed\nlength of `b.shape[-1]` characters.\n\noptional kwarg `encoding` can be used to specify character encoding (default\n`utf-8`). If `encoding` is 'none' or 'bytes', a `numpy.string_` btye array is\nreturned.\n\nreturns a numpy string array with datatype `'UN'` (or `'SN'`) and shape\n`b.shape[:-1]` where where `N=b.shape[-1]`."
    pass

def date2index(dates, nctime, calendar=None, select='exact'):
    "date2index(dates, nctime, calendar=None, select='exact')\n\n    Return indices of a netCDF time variable corresponding to the given dates.\n\n    **`dates`**: A datetime object or a sequence of datetime objects.\n    The datetime objects should not include a time-zone offset.\n\n    **`nctime`**: A netCDF time variable object. The nctime object must have a\n    `units` attribute.\n\n    **`calendar`**: describes the calendar used in the time calculations.\n    All the values currently defined in the\n    [CF metadata convention](http://cfconventions.org)\n    Valid calendars `'standard', 'gregorian', 'proleptic_gregorian'\n    'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'`.\n    Default is `'standard'`, which is a mixed Julian/Gregorian calendar.\n    If `calendar` is None, its value is given by `nctime.calendar` or\n    `standard` if no such attribute exists.\n\n    **`select`**: `'exact', 'before', 'after', 'nearest'`\n    The index selection method. `exact` will return the indices perfectly\n    matching the dates given. `before` and `after` will return the indices\n    corresponding to the dates just before or just after the given dates if\n    an exact match cannot be found. `nearest` will return the indices that\n    correspond to the closest dates.\n\n    returns an index (indices) of the netCDF time variable corresponding\n    to the given datetime object(s).\n    "
    pass

def date2num(dates, units, calendar='standard'):
    "date2num(dates,units,calendar='standard')\n\n    Return numeric time values given datetime objects. The units\n    of the numeric time values are described by the `units` argument\n    and the `calendar` keyword. The datetime objects must\n    be in UTC with no time-zone offset.  If there is a\n    time-zone offset in `units`, it will be applied to the\n    returned numeric values.\n\n    **`dates`**: A datetime object or a sequence of datetime objects.\n    The datetime objects should not include a time-zone offset.\n\n    **`units`**: a string of the form `<time units> since <reference time>`\n    describing the time units. `<time units>` can be days, hours, minutes,\n    seconds, milliseconds or microseconds. `<reference time>` is the time\n    origin. `months_since` is allowed *only* for the `360_day` calendar.\n\n    **`calendar`**: describes the calendar used in the time calculations.\n    All the values currently defined in the\n    [CF metadata convention](http://cfconventions.org)\n    Valid calendars `'standard', 'gregorian', 'proleptic_gregorian'\n    'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'`.\n    Default is `'standard'`, which is a mixed Julian/Gregorian calendar.\n\n    returns a numeric time value, or an array of numeric time values\n    with approximately 10 microsecond accuracy.\n        "
    pass

default_encoding = 'utf-8'
default_fillvals = _mod_builtins.dict()
def getlibversion():
    '\n**`getlibversion()`**\n\nreturns a string describing the version of the netcdf library\nused to build the module, and when it was built.\n    '
    pass

def glob(pathname):
    "Return a list of paths matching a pathname pattern.\n\n    The pattern may contain simple shell-style wildcards a la\n    fnmatch. However, unlike fnmatch, filenames starting with a\n    dot are special cases that are not matched by '*' and '?'\n    patterns.\n\n    If recursive is true, the pattern '**' will match any files and\n    zero or more directories and subdirectories.\n    "
    pass

is_native_big = False
is_native_little = True
def num2date(times, units, calendar='standard'):
    "num2date(times,units,calendar='standard')\n\n    Return datetime objects given numeric time values. The units\n    of the numeric time values are described by the `units` argument\n    and the `calendar` keyword. The returned datetime objects represent\n    UTC with no time-zone offset, even if the specified\n    `units` contain a time-zone offset.\n\n    **`times`**: numeric time values.\n\n    **`units`**: a string of the form `<time units> since <reference time>`\n    describing the time units. `<time units>` can be days, hours, minutes,\n    seconds, milliseconds or microseconds. `<reference time>` is the time\n    origin. `months_since` is allowed *only* for the `360_day` calendar.\n\n    **`calendar`**: describes the calendar used in the time calculations.\n    All the values currently defined in the\n    [CF metadata convention](http://cfconventions.org)\n    Valid calendars `'standard', 'gregorian', 'proleptic_gregorian'\n    'noleap', '365_day', '360_day', 'julian', 'all_leap', '366_day'`.\n    Default is `'standard'`, which is a mixed Julian/Gregorian calendar.\n\n    **`only_use_cftime_datetimes`**: if False (default), datetime.datetime\n    objects are returned from num2date where possible; if True dates which\n    subclass cftime.datetime are returned for all calendars.\n\n    returns a datetime instance, or an array of datetime instances with\n    approximately 10 microsecond accuracy.\n\n    ***Note***: The datetime instances returned are 'real' python datetime\n    objects if `calendar='proleptic_gregorian'`, or\n    `calendar='standard'` or `'gregorian'`\n    and the date is after the breakpoint between the Julian and\n    Gregorian calendars (1582-10-15). Otherwise, they are 'phony' datetime\n    objects which support some but not all the methods of 'real' python\n    datetime objects. The datetime instances\n    do not contain a time-zone offset, even if the specified `units`\n    contains one.\n    "
    pass

python3 = True
def stringtoarr():
    "\n**`stringtoarr(a, NUMCHARS,dtype='S')`**\n\nconvert a string to a character array of length `NUMCHARS`\n\n**`a`**:  Input python string.\n\n**`NUMCHARS`**:  number of characters used to represent string\n(if len(a) < `NUMCHARS`, it will be padded on the right with blanks).\n\n**`dtype`**:  type of numpy array to return.  Default is `'S'`, which\nmeans an array of dtype `'S1'` will be returned.  If dtype=`'U'`, a\nunicode array (dtype = `'U1'`) will be returned.\n\nreturns a rank 1 numpy character array of length NUMCHARS with datatype `'S1'`\n(default) or `'U1'` (if dtype=`'U'`)"
    pass

def stringtochar():
    "\n**`stringtochar(a,encoding='utf-8')`**\n\nconvert a string array to a character array with one extra dimension\n\n**`a`**:  Input numpy string array with numpy datatype `'SN'` or `'UN'`, where N\nis the number of characters in each string.  Will be converted to\nan array of characters (datatype `'S1'` or `'U1'`) of shape `a.shape + (N,)`.\n\noptional kwarg `encoding` can be used to specify character encoding (default\n`utf-8`). If `encoding` is 'none' or 'bytes', a `numpy.string_` the input array\nis treated a raw byte strings (`numpy.string_`).\n\nreturns a numpy character array with datatype `'S1'` or `'U1'`\nand shape `a.shape + (N,)`, where N is the length of each string in a."
    pass

unicode_error = 'replace'
import builtins as _mod_builtins
import numpy as _mod_numpy
import scipy.sparse.csr as _mod_scipy_sparse_csr

DTYPE = _mod_numpy.float64
ITYPE = _mod_numpy.int32
__builtins__ = {}
__doc__ = '\nTools and utilities for working with compressed sparse graphs\n'
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/scipy/sparse/csgraph/_tools.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.sparse.csgraph._tools'
__package__ = 'scipy.sparse.csgraph'
__test__ = _mod_builtins.dict()
def construct_dist_matrix():
    '\n    construct_dist_matrix(graph, predecessors, directed=True, null_value=np.inf)\n\n    Construct distance matrix from a predecessor matrix\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    graph : array_like or sparse\n        The N x N matrix representation of a directed or undirected graph.\n        If dense, then non-edges are indicated by zeros or infinities.\n    predecessors : array_like\n        The N x N matrix of predecessors of each node (see Notes below).\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only move from\n        point i to point j along paths csgraph[i, j].\n        If False, then operate on an undirected graph: the algorithm can\n        progress from point i to j along csgraph[i, j] or csgraph[j, i].\n    null_value : bool, optional\n        value to use for distances between unconnected nodes.  Default is\n        np.inf\n\n    Returns\n    -------\n    dist_matrix : ndarray\n        The N x N matrix of distances between nodes along the path specified\n        by the predecessor matrix.  If no path exists, the distance is zero.\n\n    Notes\n    -----\n    The predecessor matrix is of the form returned by\n    :func:`graph_shortest_path`.  Row i of the predecessor matrix contains\n    information on the shortest paths from point i: each entry\n    predecessors[i, j] gives the index of the previous node in the path from\n    point i to point j.  If no path exists between point i and j, then\n    predecessors[i, j] = -9999\n    '
    pass

def csgraph_from_dense():
    '\n    csgraph_from_dense(graph, null_value=0, nan_null=True, infinity_null=True)\n\n    Construct a CSR-format sparse graph from a dense matrix.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    graph : array_like\n        Input graph.  Shape should be (n_nodes, n_nodes).\n    null_value : float or None (optional)\n        Value that denotes non-edges in the graph.  Default is zero.\n    infinity_null : bool\n        If True (default), then infinite entries (both positive and negative)\n        are treated as null edges.\n    nan_null : bool\n        If True (default), then NaN entries are treated as non-edges\n\n    Returns\n    -------\n    csgraph : csr_matrix\n        Compressed sparse representation of graph,\n    '
    pass

def csgraph_from_masked():
    '\n    csgraph_from_masked(graph)\n\n    Construct a CSR-format graph from a masked array.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    graph : MaskedArray\n        Input graph.  Shape should be (n_nodes, n_nodes).\n\n    Returns\n    -------\n    csgraph : csr_matrix\n        Compressed sparse representation of graph,\n    '
    pass

def csgraph_masked_from_dense():
    '\n    csgraph_masked_from_dense(graph, null_value=0, nan_null=True,\n                              infinity_null=True, copy=True)\n\n    Construct a masked array graph representation from a dense matrix.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    graph : array_like\n        Input graph.  Shape should be (n_nodes, n_nodes).\n    null_value : float or None (optional)\n        Value that denotes non-edges in the graph.  Default is zero.\n    infinity_null : bool\n        If True (default), then infinite entries (both positive and negative)\n        are treated as null edges.\n    nan_null : bool\n        If True (default), then NaN entries are treated as non-edges\n\n    Returns\n    -------\n    csgraph : MaskedArray\n        masked array representation of graph\n    '
    pass

def csgraph_to_dense():
    "\n    csgraph_to_dense(csgraph, null_value=0)\n\n    Convert a sparse graph representation to a dense representation\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : csr_matrix, csc_matrix, or lil_matrix\n        Sparse representation of a graph.\n    null_value : float, optional\n        The value used to indicate null edges in the dense representation.\n        Default is 0.\n\n    Returns\n    -------\n    graph : ndarray\n        The dense representation of the sparse graph.\n\n    Notes\n    -----\n    For normal sparse graph representations, calling csgraph_to_dense with\n    null_value=0 produces an equivalent result to using dense format\n    conversions in the main sparse package.  When the sparse representations\n    have repeated values, however, the results will differ.  The tools in\n    scipy.sparse will add repeating values to obtain a final value.  This\n    function will select the minimum among repeating values to obtain a\n    final value.  For example, here we'll create a two-node directed sparse\n    graph with multiple edges from node 0 to node 1, of weights 2 and 3.\n    This illustrates the difference in behavior:\n\n    >>> from scipy.sparse import csr_matrix, csgraph\n    >>> data = np.array([2, 3])\n    >>> indices = np.array([1, 1])\n    >>> indptr = np.array([0, 2, 2])\n    >>> M = csr_matrix((data, indices, indptr), shape=(2, 2))\n    >>> M.toarray()\n    array([[0, 5],\n           [0, 0]])\n    >>> csgraph.csgraph_to_dense(M)\n    array([[0., 2.],\n           [0., 0.]])\n\n    The reason for this difference is to allow a compressed sparse graph to\n    represent multiple edges between any two nodes.  As most sparse graph\n    algorithms are concerned with the single lowest-cost edge between any\n    two nodes, the default scipy.sparse behavior of summming multiple weights\n    does not make sense in this context.\n\n    The other reason for using this routine is to allow for graphs with\n    zero-weight edges.  Let's look at the example of a two-node directed\n    graph, connected by an edge of weight zero:\n\n    >>> from scipy.sparse import csr_matrix, csgraph\n    >>> data = np.array([0.0])\n    >>> indices = np.array([1])\n    >>> indptr = np.array([0, 1, 1])\n    >>> M = csr_matrix((data, indices, indptr), shape=(2, 2))\n    >>> M.toarray()\n    array([[0, 0],\n           [0, 0]])\n    >>> csgraph.csgraph_to_dense(M, np.inf)\n    array([[ inf,   0.],\n           [ inf,  inf]])\n\n    In the first case, the zero-weight edge gets lost in the dense\n    representation.  In the second case, we can choose a different null value\n    and see the true form of the graph.\n    "
    pass

def csgraph_to_masked():
    '\n    csgraph_to_masked(csgraph)\n\n    Convert a sparse graph representation to a masked array representation\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : csr_matrix, csc_matrix, or lil_matrix\n        Sparse representation of a graph.\n\n    Returns\n    -------\n    graph : MaskedArray\n        The masked dense representation of the sparse graph.\n    '
    pass

csr_matrix = _mod_scipy_sparse_csr.csr_matrix
def isspmatrix(x):
    'Is x of a sparse matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a sparse matrix\n\n    Returns\n    -------\n    bool\n        True if x is a sparse matrix, False otherwise\n\n    Notes\n    -----\n    issparse and isspmatrix are aliases for the same function.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix\n    >>> isspmatrix(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import isspmatrix\n    >>> isspmatrix(5)\n    False\n    '
    pass

def isspmatrix_csc(x):
    'Is x of csc_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csc matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csc matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csc_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csc_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csr_matrix([[5]]))\n    False\n    '
    pass

def isspmatrix_csr(x):
    'Is x of csr_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csr matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csr matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix_csr\n    >>> isspmatrix_csr(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csr(csc_matrix([[5]]))\n    False\n    '
    pass

def isspmatrix_lil(x):
    'Is x of lil_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a lil matrix\n\n    Returns\n    -------\n    bool\n        True if x is a lil matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import lil_matrix, isspmatrix_lil\n    >>> isspmatrix_lil(lil_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import lil_matrix, csr_matrix, isspmatrix_lil\n    >>> isspmatrix_lil(csr_matrix([[5]]))\n    False\n    '
    pass

def reconstruct_path():
    '\n    reconstruct_path(csgraph, predecessors, directed=True)\n\n    Construct a tree from a graph and a predecessor list.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix\n        The N x N matrix representing the directed or undirected graph\n        from which the predecessors are drawn.\n    predecessors : array_like, one dimension\n        The length-N array of indices of predecessors for the tree.  The\n        index of the parent of node i is given by predecessors[i].\n    directed : bool, optional\n        If True (default), then operate on a directed graph: only move from\n        point i to point j along paths csgraph[i, j].\n        If False, then operate on an undirected graph: the algorithm can\n        progress from point i to j along csgraph[i, j] or csgraph[j, i].\n\n    Returns\n    -------\n    cstree : csr matrix\n        The N x N directed compressed-sparse representation of the tree drawn\n        from csgraph which is encoded by the predecessor list.\n    '
    pass


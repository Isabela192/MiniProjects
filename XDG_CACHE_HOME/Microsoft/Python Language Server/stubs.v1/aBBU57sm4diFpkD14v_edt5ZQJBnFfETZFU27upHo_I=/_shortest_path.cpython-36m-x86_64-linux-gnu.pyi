import builtins as _mod_builtins
import numpy as _mod_numpy
import scipy.sparse.csr as _mod_scipy_sparse_csr

DTYPE = _mod_numpy.float64
ITYPE = _mod_numpy.int32
class NegativeCycleError(_mod_builtins.Exception):
    __class__ = NegativeCycleError
    __dict__ = {}
    def __init__(self, message):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'scipy.sparse.csgraph._shortest_path'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

__builtins__ = {}
__doc__ = "\nRoutines for performing shortest-path graph searches\n\nThe main interface is in the function :func:`shortest_path`.  This\ncalls cython routines that compute the shortest path using\nthe Floyd-Warshall algorithm, Dijkstra's algorithm with Fibonacci Heaps,\nthe Bellman-Ford algorithm, or Johnson's Algorithm.\n"
__file__ = '/home/isabela/anaconda3/envs/radar/lib/python3.6/site-packages/scipy/sparse/csgraph/_shortest_path.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'scipy.sparse.csgraph._shortest_path'
__package__ = 'scipy.sparse.csgraph'
__test__ = _mod_builtins.dict()
def bellman_ford():
    "\n    bellman_ford(csgraph, directed=True, indices=None, return_predecessors=False,\n                 unweighted=False)\n\n    Compute the shortest path lengths using the Bellman-Ford algorithm.\n\n    The Bellman-ford algorithm can robustly deal with graphs with negative\n    weights.  If a negative cycle is detected, an error is raised.  For\n    graphs without negative edge weights, dijkstra's algorithm may be faster.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array, matrix, or sparse matrix, 2 dimensions\n        The N x N array of distances representing the input graph.\n    directed : bool, optional\n        If True (default), then find the shortest path on a directed graph:\n        only move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i]\n    indices : array_like or int, optional\n        if specified, only compute the paths for the points at the given\n        indices.\n    return_predecessors : bool, optional\n        If True, return the size (N, N) predecesor matrix\n    unweighted : bool, optional\n        If True, then find unweighted distances.  That is, rather than finding\n        the path between each point such that the sum of weights is minimized,\n        find the path such that the number of edges is minimized.\n\n    Returns\n    -------\n    dist_matrix : ndarray\n        The N x N matrix of distances between graph nodes. dist_matrix[i,j]\n        gives the shortest distance from point i to point j along the graph.\n\n    predecessors : ndarray\n        Returned only if return_predecessors == True.\n        The N x N matrix of predecessors, which can be used to reconstruct\n        the shortest paths.  Row i of the predecessor matrix contains\n        information on the shortest paths from point i: each entry\n        predecessors[i, j] gives the index of the previous node in the\n        path from point i to point j.  If no path exists between point\n        i and j, then predecessors[i, j] = -9999\n\n    Raises\n    ------\n    NegativeCycleError:\n        if there are negative cycles in the graph\n\n    Notes\n    -----\n    This routine is specially designed for graphs with negative edge weights.\n    If all edge weights are positive, then Dijkstra's algorithm is a better\n    choice.\n    "
    pass

csr_matrix = _mod_scipy_sparse_csr.csr_matrix
def dijkstra():
    "\n    dijkstra(csgraph, directed=True, indices=None, return_predecessors=False,\n             unweighted=False, limit=np.inf)\n\n    Dijkstra algorithm using Fibonacci Heaps\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array, matrix, or sparse matrix, 2 dimensions\n        The N x N array of non-negative distances representing the input graph.\n    directed : bool, optional\n        If True (default), then find the shortest path on a directed graph:\n        only move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i]\n    indices : array_like or int, optional\n        if specified, only compute the paths for the points at the given\n        indices.\n    return_predecessors : bool, optional\n        If True, return the size (N, N) predecesor matrix\n    unweighted : bool, optional\n        If True, then find unweighted distances.  That is, rather than finding\n        the path between each point such that the sum of weights is minimized,\n        find the path such that the number of edges is minimized.\n    limit : float, optional\n        The maximum distance to calculate, must be >= 0. Using a smaller limit\n        will decrease computation time by aborting calculations between pairs\n        that are separated by a distance > limit. For such pairs, the distance\n        will be equal to np.inf (i.e., not connected).\n\n        .. versionadded:: 0.14.0\n\n    Returns\n    -------\n    dist_matrix : ndarray\n        The matrix of distances between graph nodes. dist_matrix[i,j]\n        gives the shortest distance from point i to point j along the graph.\n\n    predecessors : ndarray\n        Returned only if return_predecessors == True.\n        The matrix of predecessors, which can be used to reconstruct\n        the shortest paths.  Row i of the predecessor matrix contains\n        information on the shortest paths from point i: each entry\n        predecessors[i, j] gives the index of the previous node in the\n        path from point i to point j.  If no path exists between point\n        i and j, then predecessors[i, j] = -9999\n\n    Notes\n    -----\n    As currently implemented, Dijkstra's algorithm does not work for\n    graphs with direction-dependent distances when directed == False.\n    i.e., if csgraph[i,j] and csgraph[j,i] are not equal and\n    both are nonzero, setting directed=False will not yield the correct\n    result.\n\n    Also, this routine does not work for graphs with negative\n    distances.  Negative distances can lead to infinite cycles that must\n    be handled by specialized algorithms such as Bellman-Ford's algorithm\n    or Johnson's algorithm.\n    "
    pass

def floyd_warshall():
    '\n    floyd_warshall(csgraph, directed=True, return_predecessors=False,\n                   unweighted=False, overwrite=False)\n\n    Compute the shortest path lengths using the Floyd-Warshall algorithm\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array, matrix, or sparse matrix, 2 dimensions\n        The N x N array of distances representing the input graph.\n    directed : bool, optional\n        If True (default), then find the shortest path on a directed graph:\n        only move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i]\n    return_predecessors : bool, optional\n        If True, return the size (N, N) predecesor matrix\n    unweighted : bool, optional\n        If True, then find unweighted distances.  That is, rather than finding\n        the path between each point such that the sum of weights is minimized,\n        find the path such that the number of edges is minimized.\n    overwrite : bool, optional\n        If True, overwrite csgraph with the result.  This applies only if\n        csgraph is a dense, c-ordered array with dtype=float64.\n\n    Returns\n    -------\n    dist_matrix : ndarray\n        The N x N matrix of distances between graph nodes. dist_matrix[i,j]\n        gives the shortest distance from point i to point j along the graph.\n\n    predecessors : ndarray\n        Returned only if return_predecessors == True.\n        The N x N matrix of predecessors, which can be used to reconstruct\n        the shortest paths.  Row i of the predecessor matrix contains\n        information on the shortest paths from point i: each entry\n        predecessors[i, j] gives the index of the previous node in the\n        path from point i to point j.  If no path exists between point\n        i and j, then predecessors[i, j] = -9999\n\n    Raises\n    ------\n    NegativeCycleError:\n        if there are negative cycles in the graph\n    '
    pass

def isspmatrix(x):
    'Is x of a sparse matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a sparse matrix\n\n    Returns\n    -------\n    bool\n        True if x is a sparse matrix, False otherwise\n\n    Notes\n    -----\n    issparse and isspmatrix are aliases for the same function.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix\n    >>> isspmatrix(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import isspmatrix\n    >>> isspmatrix(5)\n    False\n    '
    pass

def isspmatrix_csc(x):
    'Is x of csc_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csc matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csc matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csc_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csc_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csc(csr_matrix([[5]]))\n    False\n    '
    pass

def isspmatrix_csr(x):
    'Is x of csr_matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a csr matrix\n\n    Returns\n    -------\n    bool\n        True if x is a csr matrix, False otherwise\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix_csr\n    >>> isspmatrix_csr(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc\n    >>> isspmatrix_csr(csc_matrix([[5]]))\n    False\n    '
    pass

def johnson():
    "\n    johnson(csgraph, directed=True, indices=None, return_predecessors=False,\n            unweighted=False)\n\n    Compute the shortest path lengths using Johnson's algorithm.\n\n    Johnson's algorithm combines the Bellman-Ford algorithm and Dijkstra's\n    algorithm to quickly find shortest paths in a way that is robust to\n    the presence of negative cycles.  If a negative cycle is detected,\n    an error is raised.  For graphs without negative edge weights,\n    dijkstra() may be faster.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array, matrix, or sparse matrix, 2 dimensions\n        The N x N array of distances representing the input graph.\n    directed : bool, optional\n        If True (default), then find the shortest path on a directed graph:\n        only move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i]\n    indices : array_like or int, optional\n        if specified, only compute the paths for the points at the given\n        indices.\n    return_predecessors : bool, optional\n        If True, return the size (N, N) predecesor matrix\n    unweighted : bool, optional\n        If True, then find unweighted distances.  That is, rather than finding\n        the path between each point such that the sum of weights is minimized,\n        find the path such that the number of edges is minimized.\n\n    Returns\n    -------\n    dist_matrix : ndarray\n        The N x N matrix of distances between graph nodes. dist_matrix[i,j]\n        gives the shortest distance from point i to point j along the graph.\n\n    predecessors : ndarray\n        Returned only if return_predecessors == True.\n        The N x N matrix of predecessors, which can be used to reconstruct\n        the shortest paths.  Row i of the predecessor matrix contains\n        information on the shortest paths from point i: each entry\n        predecessors[i, j] gives the index of the previous node in the\n        path from point i to point j.  If no path exists between point\n        i and j, then predecessors[i, j] = -9999\n\n    Raises\n    ------\n    NegativeCycleError:\n        if there are negative cycles in the graph\n\n    Notes\n    -----\n    This routine is specially designed for graphs with negative edge weights.\n    If all edge weights are positive, then Dijkstra's algorithm is a better\n    choice.\n    "
    pass

def shortest_path():
    "\n    shortest_path(csgraph, method='auto', directed=True, return_predecessors=False,\n                  unweighted=False, overwrite=False, indices=None)\n\n    Perform a shortest-path graph search on a positive directed or\n    undirected graph.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array, matrix, or sparse matrix, 2 dimensions\n        The N x N array of distances representing the input graph.\n    method : string ['auto'|'FW'|'D'], optional\n        Algorithm to use for shortest paths.  Options are:\n\n           'auto' -- (default) select the best among 'FW', 'D', 'BF', or 'J'\n                     based on the input data.\n\n           'FW'   -- Floyd-Warshall algorithm.  Computational cost is\n                     approximately ``O[N^3]``.  The input csgraph will be\n                     converted to a dense representation.\n\n           'D'    -- Dijkstra's algorithm with Fibonacci heaps.  Computational\n                     cost is approximately ``O[N(N*k + N*log(N))]``, where\n\t\t     ``k`` is the average number of connected edges per node.\n\t\t     The input csgraph will be converted to a csr\n\t\t     representation.\n\n           'BF'   -- Bellman-Ford algorithm.  This algorithm can be used when\n                     weights are negative.  If a negative cycle is encountered,\n                     an error will be raised.  Computational cost is\n                     approximately ``O[N(N^2 k)]``, where ``k`` is the average\n                     number of connected edges per node. The input csgraph will\n                     be converted to a csr representation.\n\n           'J'    -- Johnson's algorithm.  Like the Bellman-Ford algorithm,\n                     Johnson's algorithm is designed for use when the weights\n                     are negative.  It combines the Bellman-Ford algorithm\n                     with Dijkstra's algorithm for faster computation.\n\n    directed : bool, optional\n        If True (default), then find the shortest path on a directed graph:\n        only move from point i to point j along paths csgraph[i, j].\n        If False, then find the shortest path on an undirected graph: the\n        algorithm can progress from point i to j along csgraph[i, j] or\n        csgraph[j, i]\n    return_predecessors : bool, optional\n        If True, return the size (N, N) predecesor matrix\n    unweighted : bool, optional\n        If True, then find unweighted distances.  That is, rather than finding\n        the path between each point such that the sum of weights is minimized,\n        find the path such that the number of edges is minimized.\n    overwrite : bool, optional\n        If True, overwrite csgraph with the result.  This applies only if\n        method == 'FW' and csgraph is a dense, c-ordered array with\n        dtype=float64.\n    indices : array_like or int, optional\n        If specified, only compute the paths for the points at the given\n        indices. Incompatible with method == 'FW'.\n\n    Returns\n    -------\n    dist_matrix : ndarray\n        The N x N matrix of distances between graph nodes. dist_matrix[i,j]\n        gives the shortest distance from point i to point j along the graph.\n\n    predecessors : ndarray\n        Returned only if return_predecessors == True.\n        The N x N matrix of predecessors, which can be used to reconstruct\n        the shortest paths.  Row i of the predecessor matrix contains\n        information on the shortest paths from point i: each entry\n        predecessors[i, j] gives the index of the previous node in the\n        path from point i to point j.  If no path exists between point\n        i and j, then predecessors[i, j] = -9999\n\n    Raises\n    ------\n    NegativeCycleError:\n        if there are negative cycles in the graph\n\n    Notes\n    -----\n    As currently implemented, Dijkstra's algorithm and Johnson's algorithm\n    do not work for graphs with direction-dependent distances when\n    directed == False.  i.e., if csgraph[i,j] and csgraph[j,i] are non-equal\n    edges, method='D' may yield an incorrect result.\n    "
    pass

def validate_graph(csgraph, directed, dtype, csr_output, dense_output, copy_if_dense, copy_if_sparse, null_value_in, null_value_out, infinity_null, nan_null):
    'Routine for validation and conversion of csgraph inputs'
    pass


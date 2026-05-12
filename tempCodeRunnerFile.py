    >>> X, Y = datasets.load_nonlinear_example1()
    >>> ex_X = datasets.polynomial2_features(X)
    >>> ex_X
    array([[ 1.  ,  0.  ,  0.  ],
          [ 1.  ,  2.  ,  4.  ],
          [ 1.  ,  3.9 , 15.21],
          [ 1.  ,  4.  , 16.  ]])
    >>> Y
    array([ 4.,  0.,  3.,  2.])
import numpy as np

test = {
  'name': 'Question fake_diffs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'fake_diffs'
          >>> 'fake_diffs' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'fake_diffs'
          >>> # from its initial state (of ...)
          >>> fake_diffs is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(fake_diffs)
          10000
          """,
          'hidden': False,
          'locked': False
        },
        {
          # See calc_limits.py
          'code': r"""
          >>> np.all(np.logical_and(fake_diffs < 13.4, fake_diffs > -13.4))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> mu = np.mean(fake_diffs)
          >>> -0.1 < mu < 0.1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sd = np.std(fake_diffs)
          >>> 2.89 < sd < 3.03
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

test = {
  'name': 'Question afters',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'afters'
          >>> 'afters' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'afters'
          >>> # from its initial state (of ...)
          >>> afters is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(afters, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(afters) == np.count_nonzero(mosquitoes['test'] == 'after')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you make the new column?
          >>> 'volunt_diff' in afters
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(afters['volunt_diff'] ==
          ...        afters['volunt_odour'] - afters['no_odour'])
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

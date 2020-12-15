test = {
  'name': 'Question after_arrs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the values for the arrays.
          >>> 'after_beer_vd' in vars()
          True
          >>> 'after_water_vd' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the values
          >>> # from their initial states (of ...)
          >>> after_beer_vd is not ...
          True
          >>> after_water_vd is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The values should be arrays
          >>> isinstance(after_beer_vd, np.ndarray)
          True
          >>> isinstance(after_water_vd, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(after_beer_vd) == 25
          True
          >>> len(after_water_vd) == 18
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.sum(after_beer_vd) == 148
          True
          >>> np.sum(after_water_vd) == -23
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

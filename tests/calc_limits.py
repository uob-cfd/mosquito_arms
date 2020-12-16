""" Calculate limits for tests
"""

import os.path as op
import numpy as np
import pandas as pd


def get_data():
    ex_dir = op.join(op.dirname(__file__), '..')
    mosquitoes = pd.read_csv(op.join(ex_dir, 'mosquito_beer.csv'))
    afters = mosquitoes[mosquitoes['test'] == 'after'].copy()
    afters['volunt_diff'] = afters['volunt_odour'] - afters['no_odour']
    after_beer = afters[afters['group'] == 'beer']
    after_beer_vd = np.array(after_beer['volunt_diff'])
    after_water = afters[afters['group'] == 'water']
    after_water_vd = np.array(after_water['volunt_diff'])
    return after_beer_vd, after_water_vd


def for_limits(n_iters=10000, n_repeats=1000):
    after_beer_vd, after_water_vd = get_data()
    pooled = np.append(after_beer_vd, after_water_vd)
    n_beer = len(after_beer_vd)
    n_all = n_iters * n_repeats
    fake_diffs = np.zeros(n_all)
    for i in range(n_all):
        shuffled = np.random.permutation(pooled)
        fake_diffs[i] = np.mean(shuffled[:n_beer]) - np.mean(shuffled[n_beer:])
    fds = fake_diffs.reshape((n_iters, n_repeats))
    return fds


def get_fd_limits(fake_diffs):
    import numpy as np
    print('Value range', np.quantile(fake_diffs, [0, 1]))
    print('Mean range', np.quantile(np.mean(fake_diffs, axis=0), [0, 1]))
    print('SD range', np.quantile(np.std(fake_diffs, axis=0), [0, 1]))


def get_p_limits(fake_diffs):
    after_beer_vd, after_water_vd = get_data()
    beer_mean = np.mean(after_beer_vd)
    water_mean = np.mean(after_water_vd)
    beer_water_diff = beer_mean - water_mean
    counts = np.count_nonzero(fake_diffs >= beer_water_diff, axis=0)
    ps = counts / fake_diffs.shape[0]
    return np.quantile(ps, [0, 1])

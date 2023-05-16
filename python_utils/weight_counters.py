import numpy as np


def steriade_vowels(nseg, cmu_segs):
    """Implements weight counts that
    count all segments except word initial onsets
    and word final codas."""
    if type(cmu_segs) == str:
        counter = 0
        for seg in cmu_segs.split(' '):
            if seg[-1] not in ('0', '1', '2'):
                counter += 1
            else:
                break
        for seg in reversed(cmu_segs.split(' ')):
            if seg[-1] not in ('0', '1', '2'):
                counter += 1
            else:
                break
        return nseg - counter
    else:
        return np.nan


def count_weight(weight):
    if type(weight) == str:
        return len(weight.replace('L', ''))
    else:
        return np.nan


def check_weight_stress(stress, weight):
    if type(stress) == str:
        try:
            if weight[stress.index('P')] == 'H':
                return True
            else:
                return False
        except ValueError:
            return False
    else:
        return False


def steriade_consonants(cmu_segs):
    """
    Finds aggregate of inter syllabic
    periods.
    :param cmu_segs:
    :return:
    """
    if type(cmu_segs) == str:
        counter = 0
        for idx, seg in enumerate(cmu_segs.split(' ')):
            if seg[-1] not in ('0', '1', '2'):
                pass
            else:
                start_idx = idx
                break

        for idx, seg in enumerate(reversed(cmu_segs.split(' '))):
            if seg[-1] not in ('0', '1', '2'):
                pass
            else:
                end_idx = idx
                break

        for seg in cmu_segs.split(' ')[start_idx+1:-end_idx]:
            if seg[-1] not in ('0', '1', '2'):
                counter += 1

        return counter

    else:
        return np.nan
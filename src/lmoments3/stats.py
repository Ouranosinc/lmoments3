"""Statistics functions for L-moments analysis."""

# lmoments3 library
# Copyright (C) 2012, 2014 J. R. M. Hosking, William Asquith,
# Sam Gillespie, Pierre Gérard-Marchant, Florenz A. P. Hollebrandse
#
# Copyright (C) 2023 Ouranos Inc., Trevor James Smith, Pascal Bourgault
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math

from . import distr


def AIC(data, distr_name, distr_paras):  # noqa: N802
    """Calculate the Akaike Information Criterion (AIC)."""
    distr_f = getattr(distr, distr_name.lower())  # scipy rv_continous class

    NLL = distr_f.nnlf(data, **distr_paras)
    k = (
        distr_f.numargs + 2
    )  # Include location and scale in addition to shape parameters
    AIC = 2 * k + 2 * NLL
    return AIC


def AICc(data, distr_name, distr_paras):  # noqa: N802
    """Calculate the corrected Akaike Information Criterion (AICc)."""
    distr_f = getattr(distr, distr_name.lower())  # scipy rv_continous class

    AICbase = AIC(data, distr_name, distr_paras)
    k = (
        distr_f.numargs + 2
    )  # Include location and scale in addition to shape parameters
    diff = 2 * k * (k + 1) / (len(data) - k - 1)
    AICc = AICbase + diff
    return AICc


def BIC(data, distr_name, distr_paras):  # noqa: N802
    """Calculate the Bayesian Information Criterion (BIC)."""
    distr_f = getattr(distr, distr_name.lower())  # scipy rv_continous class

    NLL = distr_f.nnlf(data, **distr_paras)
    k = (
        distr_f.numargs + 2
    )  # Include location and scale in addition to shape parameters
    BIC = k * math.log(len(data)) + 2 * NLL
    return BIC

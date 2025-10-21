from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


def to_month_start(date_series: pd.Series) -> pd.Series:
    """Converte uma coluna de datas para o primeiro dia do mês (timestamp mensal).

    Args:
        date_series: Série com datas (strings ou datetime-like).

    Returns:
        pd.Series com datas normalizadas para o início do mês (ns).
    """
    series_as_datetime = pd.to_datetime(date_series)
    # Converte para período mensal e volta para timestamp no início do mês
    return series_as_datetime.values.astype("datetime64[M]").astype("datetime64[ns]")


def monthly_ipca_to_annualized(ipca_mom_pct: pd.Series) -> pd.Series:
    """Converte inflação mensal (%) para anualizada (%) por composição: (1+π_m)^12 - 1.

    Args:
        ipca_mom_pct: Série com inflação mensal em porcentagem (% ao mês).

    Returns:
        pd.Series com inflação anualizada em porcentagem (% a.a.).
    """
    monthly_fraction = ipca_mom_pct / 100.0
    annual_fraction = (1.0 + monthly_fraction) ** 12 - 1.0
    return annual_fraction * 100.0


def fisher_approx(nominal_aa_pct: pd.Series, inflation_aa_pct: pd.Series) -> pd.Series:
    """Taxa real aproximada (em % a.a.): r ≈ i - π.

    Args:
        nominal_aa_pct: Taxa nominal anual em porcentagem (% a.a.).
        inflation_aa_pct: Inflação anual em porcentagem (% a.a.).

    Returns:
        pd.Series com taxa real aproximada em porcentagem (% a.a.).
    """
    nominal_fraction = nominal_aa_pct / 100.0
    inflation_fraction = inflation_aa_pct / 100.0
    real_fraction = nominal_fraction - inflation_fraction
    return real_fraction * 100.0


def fisher_exact(nominal_aa_pct: pd.Series, inflation_aa_pct: pd.Series) -> pd.Series:
    """Taxa real exata (em % a.a.): (1+r) = (1+i)/(1+π) ⇒ r = (1+i)/(1+π) - 1.

    Args:
        nominal_aa_pct: Taxa nominal anual em porcentagem (% a.a.).
        inflation_aa_pct: Inflação anual em porcentagem (% a.a.).

    Returns:
        pd.Series com taxa real exata em porcentagem (% a.a.).
    """
    nominal_fraction = nominal_aa_pct / 100.0
    inflation_fraction = inflation_aa_pct / 100.0
    real_fraction = (1.0 + nominal_fraction) / (1.0 + inflation_fraction) - 1.0
    return real_fraction * 100.0

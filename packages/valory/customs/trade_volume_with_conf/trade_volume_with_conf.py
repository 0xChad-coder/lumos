"""This module contains a strategy that calculates the trade volume based on the trader's confidence level."""

from typing import Union, List, Dict, Tuple, Any

REQUIRED_FIELDS = ("confidence", "volume_per_confidence")

def check_missing_fields(kwargs: Dict[str, Any]) -> List[str]:
    """Check for missing fields and return them, if any."""
    missing = []
    for field in REQUIRED_FIELDS:
        if kwargs.get(field, None) is None:
            missing.append(field)
    return missing


def remove_irrelevant_fields(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Remove the irrelevant fields from the given kwargs."""
    return {key: value for key, value in kwargs.items() if key in REQUIRED_FIELDS}


def volume_based_on_confidence(
    confidence: float, volume_per_confidence: Dict[str, int]
) -> Dict[str, Union[int, Tuple[str]]]:
    """Calculate the trade volume based on confidence level."""
    # Convert the confidence level to a string rounded to one decimal place.
    confidence_level = str(round(confidence, 1))
    trade_volume = volume_per_confidence.get(confidence_level, None)

    if trade_volume is None:
        return {
            "error": (
                f"No trade volume found for confidence level {confidence_level} in {volume_per_confidence}.",
            )
        }
    return {"trade_volume": trade_volume}


def run(*_args, **kwargs) -> Dict[str, Union[int, Tuple[str]]]:
    """Run the strategy."""
    missing = check_missing_fields(kwargs)
    if len(missing) > 0:
        return {"error": (f"Required kwargs {missing} were not provided.",)}

    kwargs = remove_irrelevant_fields(kwargs)
    return volume_based_on_confidence(**kwargs)

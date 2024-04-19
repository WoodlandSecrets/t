"""Test cajudsa."""

import cajudsa


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(cajudsa.__name__, str)

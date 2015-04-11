"""Module for baked spitfire utility functions."""
from spitfire.runtime import _baked


class _SanitizedPlaceholder(str):
  """Class the represesnts an already sanitized string.

  SanitizedPlaceholder wraps another value to let the runtime know that this
  does not need to filtered again.
  """
  pass


def _runtime_mark_as_sanitized(value, function):
  """Wrap a function's return value in a SanitizedPlaceholder.

  This function is called often so it needs to be fast. This
  function checks the skip_filter annotation on the function passed
  in to determine if the value should be wrapped.

  Args:
    value: The value to be marked
    function: The function to check for skip_filter

  Returns:
    Either a SanitizedPlaceholder object or the value passed in.
  """
  if getattr(function, 'skip_filter', False):
    if type(value) == str:
      return _SanitizedPlaceholder(value)
  return value


def _mark_as_sanitized(value):
  """Wrap a value in a SanitizedPlaceholder.

  This function is called often so it needs to be fast.

  Args:
    value: The value to be marked

  Returns:
    Either a SanitizedPlaceholder object or the value passed in.
  """
  # The if branch is going to be taken in most cases.
  if type(value) == str:
    return _SanitizedPlaceholder(value)
  return value


# Use C
SanitizedPlaceholder = _baked._SanitizedPlaceholder
runtime_mark_as_sanitized = _baked._runtime_mark_as_sanitized
mark_as_sanitized = _baked._mark_as_sanitized
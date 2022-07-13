# roxar_proxy

Mock library for testing purposes. Conditionally mocks based on the availability of RoxarAPI.

## Installation

```
roxenv python -m pip install git+https://github.com/RoxarAPI/roxar_proxy#egg=roxar_proxy
```

## Example

```python
import roxar_proxy as roxar

log_run = roxar.LogRun()
log_run.set_measured_depths([1., 100.])
curve = log_run.log_curves.create_discrete("DiscreteLog")
curve.set_values([1, 2])
curve.set_code_names({1: "One", 2: "Two"})
```

## Testing

Using RoxarAPI:
```python
roxenv python test.py
```

Without RoxarAPI, using mocking:
```python
python test.py
```


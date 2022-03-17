---
title: How to create custom Parameterized Expectations
---

This guide will walk you through the process of creating Parameterized <TechnicalTag tag="expectation" text="Expectations" /> - very quickly. This method is only available using the new Modular Expectations API in 0.13.

:::note Prerequisites 
This how-to guide assumes you have already:

* [Set up a working deployment of Great Expectations](/docs/tutorials/getting_started/intro)
:::

A Parameterized Expectation is a capability unlocked by Modular Expectations. Now that Expectations are structured in class form, it is easier than every before to inherit from these classes and build similar Expectations that are adapted to your own needs.

## Steps

### 1. Select an Expectation to inherit from

For the purpose of this exercise, we will implement the Expectation “expect_column_mean_to_be_positive” - a realistic Expectation of the data that can easily inherit from expect_column_mean_to_be_between.

### 2. Select default values for your class

As can be seen in the implementation below, we have chosen to keep our default minimum value at 0, given that we are validating that all our values are positive. Setting the upper bound to `None` means that no upper bound will be checked – effectively setting the threshold at ∞ and allowing any positive value.

Notice that we do not need to set `default_kwarg_values` for all kwargs: it is sufficient to set them only for ones for which we would like to set a default value. To keep our implementation simple, we do not override the `metric_dependencies` or `success_keys`.

````python
class ExpectColumnMeanToBePositive(ExpectColumnMeanToBeBetween):
   default_kwarg_values = {
       "min_value": 0,
       "strict_min": True,
   }
````

## Additional Notes

1. We could also explicitly override our parent methods to modify the behavior of our new Expectation, for example by updating the configuration validation to require the values we set as defaults not be altered.

````python
def validate_configuration(self, configuration: Optional[ExpectationConfiguration]):
    super().validate_configuration(configuration)
    assert "min_value" not in configuration.kwargs, "min_value cannot be altered"
    assert "max_value" not in configuration.kwargs, "max_value cannot be altered"
    assert "strict_min" not in configuration.kwargs, "strict_min cannot be altered"
    assert "strict_max" not in configuration.kwargs, "strict_max cannot be altered"
````

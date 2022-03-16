"""
This is a template for creating custom TableExpectations.
For detailed instructions on how to use it, please see:
    https://docs.greatexpectations.io/docs/guides/expectations/creating_custom_expectations/how_to_create_custom_table_expectations
"""

from typing import Dict, Optional

from great_expectations.core.expectation_configuration import ExpectationConfiguration
from great_expectations.exceptions import InvalidExpectationConfigurationError
from great_expectations.execution_engine import (
    ExecutionEngine,
    PandasExecutionEngine,
    SparkDFExecutionEngine,
    SqlAlchemyExecutionEngine,
)
from great_expectations.expectations.expectation import TableExpectation
from great_expectations.expectations.metrics.metric_provider import (
    MetricConfiguration,
    metric_value,
)
from great_expectations.expectations.metrics.table_metric_provider import (
    TableMetricProvider,
)


# This class defines a Metric to support your Expectation.
# For most ColumnExpectations, the main business logic for calculation will live in this class.
class TableMeetsSomeCriteria(TableMetricProvider):

    # This is the id string that will be used to reference your Metric.
    metric_name = "METRIC NAME GOES HERE"

    # This method implements the core logic for the PandasExecutionEngine
    @metric_value(engine=PandasExecutionEngine)
    def _pandas(
        cls,
        execution_engine,
        metric_domain_kwargs,
        metric_value_kwargs,
        metrics,
        runtime_configuration,
    ):
        raise NotImplementedError

    # @metric_value(engine=SqlAlchemyExecutionEngine)
    # def _sqlalchemy(
    #         cls,
    #         execution_engine,
    #         metric_domain_kwargs,
    #         metric_value_kwargs,
    #         metrics,
    #         runtime_configuration,
    # ):
    #    raise NotImplementedError

    # @metric_value(engine=SparkDFExecutionEngine)
    # def _spark(
    #         cls,
    #         execution_engine,
    #         metric_domain_kwargs,
    #         metric_value_kwargs,
    #         metrics,
    #         runtime_configuration,
    # ):
    #    raise NotImplementedError

    @classmethod
    def _get_evaluation_dependencies(
        cls,
        metric: MetricConfiguration,
        configuration: Optional[ExpectationConfiguration] = None,
        execution_engine: Optional[ExecutionEngine] = None,
        runtime_configuration: Optional[dict] = None,
    ):
        return {
            "table.columns": MetricConfiguration(
                "table.columns", metric.metric_domain_kwargs
            ),
        }


# This class defines the Expectation itself
# The main business logic for calculation lives here.
class ExpectTableToMeetSomeCriteria(TableExpectation):
    """TODO: add a docstring here"""

    # These examples will be shown in the public gallery.
    # They will also be executed as unit tests for your Expectation.
    examples = []

    # This is a tuple consisting of all Metrics necessary to evaluate the Expectation.
    metric_dependencies = ("METRIC NAME GOES HERE",)

    # This a tuple of parameter names that can affect whether the Expectation evaluates to True or False.
    success_keys = ()

    # This dictionary contains default values for any parameters that should have default values.
    default_kwarg_values = {}

    def validate_configuration(self, configuration: Optional[ExpectationConfiguration]):
        """
        Validates that a configuration has been set, and sets a configuration if it has yet to be set. Ensures that
        necessary configuration arguments have been provided for the validation of the expectation.

        Args:
            configuration (OPTIONAL[ExpectationConfiguration]): \
                An optional Expectation Configuration entry that will be used to configure the expectation
        Returns:
            True if the configuration has been validated successfully. Otherwise, raises an exception
        """

        super().validate_configuration(configuration)
        if configuration is None:
            configuration = self.configuration

        # # Check other things in configuration.kwargs and raise Exceptions if needed
        # try:
        #     assert (
        #         ...
        #     ), "message"
        #     assert (
        #         ...
        #     ), "message"
        # except AssertionError as e:
        #     raise InvalidExpectationConfigurationError(str(e))

        return True

    # This method performs a validation of your metrics against your success keys, returning a dict indicating the success or failure of the Expectation.
    def _validate(
        self,
        configuration: ExpectationConfiguration,
        metrics: Dict,
        runtime_configuration: dict = None,
        execution_engine: ExecutionEngine = None,
    ):
        raise NotImplementedError

    # This object contains metadata for display in the public Gallery
    library_metadata = {
        "tags": [],  # Tags for this Expectation in the Gallery
        "contributors": [  # Github handles for all contributors to this Expectation.
            "@your_name_here",  # Don't forget to add your github handle here!
        ],
    }


if __name__ == "__main__":
    ExpectTableToMeetSomeCriteria().print_diagnostic_checklist()

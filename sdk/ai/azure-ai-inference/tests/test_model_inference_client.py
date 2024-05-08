# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import inspect
import azure.ai.inference as sdk

from model_inference_test_base import ModelClientTestBase, ServicePreparerChatCompletions, ServicePreparerEmbeddings
from devtools_testutils import recorded_by_proxy
from azure.core.exceptions import AzureError


# The test class name needs to start with "Test" to get collected by pytest
class TestModelClient(ModelClientTestBase):

    # **********************************************************************************
    #
    #                            HAPPY PATH TESTS
    #
    # **********************************************************************************

    @ServicePreparerChatCompletions()
    @recorded_by_proxy
    def test_chat_completions_error_free(self, **kwargs):
        client = self._create_chat_client(**kwargs)
        result = client.create(messages=[sdk.models.UserMessage(content="How many feet are in a mile?")])
        self._print_chat_completions_result(result)
        self._validate_chat_completions_result(result, ["5280", "5,280"])
        client.close()

    @ServicePreparerChatCompletions()
    @recorded_by_proxy
    def test_chat_completions_streaming_error_free(self, **kwargs):
        client = self._create_chat_client(**kwargs)
        result = client.create_streaming(
            messages=[
                sdk.models.SystemMessage(content="You are a helpful assistant."),
                sdk.models.UserMessage(content="Give me 5 good reasons why I should exercise every day."),
            ]
        )
        self._validate_chat_completions_streaming_result(result)
        client.close()

    @ServicePreparerEmbeddings()
    @recorded_by_proxy
    def test_embeddings_error_free(self, **kwargs):
        client = self._create_embeddings_client(**kwargs)
        result = client.create(input=["first phrase", "second phrase", "third phrase"])
        self._print_embeddings_result(result)
        self._validate_embeddings_result(result)
        client.close()

    # **********************************************************************************
    #
    #                            ERROR TESTS
    #
    # **********************************************************************************

    @ServicePreparerChatCompletions()
    @recorded_by_proxy
    def test_chat_completion_with_auth_failure(self, **kwargs):
        client = self._create_chat_client(bad_key=True, **kwargs)
        exception_caught = False
        try:
            result = client.create(messages=[sdk.models.UserMessage(content="How many feet are in a mile?")])
        except AzureError as e:
            exception_caught = True
            print(e)
            assert hasattr(e, "status_code")
            assert e.status_code == 401
            assert "unauthorized" in e.message.lower()
        client.close()
        assert exception_caught

    @ServicePreparerChatCompletions()
    @recorded_by_proxy
    def test_embeddings_on_chat_completion_endpoint(self, **kwargs):
        client = self._create_embeddings_client_with_chat_completions_credentials(**kwargs)
        exception_caught = False
        try:
            result = client.create(input=["first phrase", "second phrase", "third phrase"])
        except AzureError as e:
            exception_caught = True
            print(e)
            assert hasattr(e, "status_code")
            assert e.status_code == 404
            assert "not found" in e.message.lower()
        client.close()
        assert exception_caught

# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
import platform
import functools

from azure.core.exceptions import HttpResponseError, ClientAuthenticationError
from testcase import TextAnalyticsTest, TextAnalyticsPreparer, get_textanalytics_client
from devtools_testutils import recorded_by_proxy
from azure.ai.textanalytics import TextAnalyticsClient


class TestEncoding(TextAnalyticsTest):
    @TextAnalyticsPreparer()
    @recorded_by_proxy
    def test_emoji(self):
        client = get_textanalytics_client()
        result = client.recognize_pii_entities(["👩 SSN: 859-98-0987"])
        assert result[0].entities[0].offset == 7

    @TextAnalyticsPreparer()
    @recorded_by_proxy
    def test_emoji_with_skin_tone_modifier(self):
        client = get_textanalytics_client()
        result = client.recognize_pii_entities(["👩🏻 SSN: 859-98-0987"])
        assert result[0].entities[0].offset == 8

    @TextAnalyticsPreparer()
    @recorded_by_proxy
    def test_emoji_family(self):
        client = get_textanalytics_client()
        result = client.recognize_pii_entities(["👩‍👩‍👧‍👧 SSN: 859-98-0987"])
        assert result[0].entities[0].offset == 13

    @TextAnalyticsPreparer()
    @recorded_by_proxy
    def test_emoji_family_with_skin_tone_modifier(self):
        client = get_textanalytics_client()
        result = client.recognize_pii_entities(["👩🏻‍👩🏽‍👧🏾‍👦🏿 SSN: 859-98-0987"])
        assert result[0].entities[0].offset == 17

    @TextAnalyticsPreparer()
    @recorded_by_proxy
    def test_diacritics_nfc(self):
        client = get_textanalytics_client()
        result = client.recognize_pii_entities(["año SSN: 859-98-0987"])
        assert result[0].entities[0].offset == 9
    
    @TextAnalyticsPreparer()
    @recorded_by_proxy
    def test_diacritics_nfd(self):
        client = get_textanalytics_client()
        result = client.recognize_pii_entities(["año SSN: 859-98-0987"])
        assert result[0].entities[0].offset == 10

    @TextAnalyticsPreparer()
    @recorded_by_proxy
    def test_korean_nfc(self):
        client = get_textanalytics_client()
        result = client.recognize_pii_entities(["아가 SSN: 859-98-0987"])
        assert result[0].entities[0].offset == 8

    @TextAnalyticsPreparer()
    @recorded_by_proxy
    def test_korean_nfd(self):
        client = get_textanalytics_client()
        result = client.recognize_pii_entities(["아가 SSN: 859-98-0987"])
        assert result[0].entities[0].offset == 8

    @TextAnalyticsPreparer()
    @recorded_by_proxy
    def test_zalgo_text(self):
        client = get_textanalytics_client()
        result = client.recognize_pii_entities(["ơ̵̧̧̢̳̘̘͕͔͕̭̟̙͎͈̞͔̈̇̒̃͋̇̅͛̋͛̎́͑̄̐̂̎͗͝m̵͍͉̗̄̏͌̂̑̽̕͝͠g̵̢̡̢̡̨̡̧̛͉̞̯̠̤̣͕̟̫̫̼̰͓̦͖̣̣͎̋͒̈́̓̒̈̍̌̓̅͑̒̓̅̅͒̿̏́͗̀̇͛̏̀̈́̀̊̾̀̔͜͠͝ͅ SSN: 859-98-0987"])


        assert result[0].entities[0].offset == 121

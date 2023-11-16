# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ContentFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Format of the content in analyzed result."""

    TEXT = "text"
    """Plain text representation of the document content without any formatting."""
    MARKDOWN = "markdown"
    """Markdown representation of the document content with section headings, tables,
    #: etc."""


class ContentSourceKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of content source."""

    URL = "url"
    """Content at a specific URL."""
    BASE64 = "base64"
    """Content represented via Base64 encoding."""
    AZURE_BLOB = "azureBlob"
    """Files in a path within an Azure Blob Storage container."""
    AZURE_BLOB_FILE_LIST = "azureBlobFileList"
    """A file list specifying individual files in an Azure Blob Storage container."""


class DocumentAnalysisFeature(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Document analysis features to enable."""

    OCR_HIGH_RESOLUTION = "ocrHighResolution"
    """Perform OCR at a higher resolution to handle documents with fine print."""
    LANGUAGES = "languages"
    """Enable the detection of the text content language."""
    BARCODES = "barcodes"
    """Enable the detection of barcodes in the document."""
    FORMULAS = "formulas"
    """Enable the detection of mathematical expressions in the document."""
    KEY_VALUE_PAIRS = "keyValuePairs"
    """Enable the detection of general key value pairs (form fields) in the document."""
    STYLE_FONT = "styleFont"
    """Enable the recognition of various font styles."""
    QUERY_FIELDS = "queryFields"
    """Enable the extraction of additional fields via the queryFields query parameter."""


class DocumentBarcodeKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Barcode kind."""

    Q_R_CODE = "QRCode"
    """QR code, as defined in ISO/IEC 18004:2015."""
    PDF417 = "PDF417"
    """PDF417, as defined in ISO 15438."""
    UPCA = "UPCA"
    """GS1 12-digit Universal Product Code."""
    UPCE = "UPCE"
    """GS1 6-digit Universal Product Code."""
    CODE39 = "Code39"
    """Code 39 barcode, as defined in ISO/IEC 16388:2007."""
    CODE128 = "Code128"
    """Code 128 barcode, as defined in ISO/IEC 15417:2007."""
    EAN8 = "EAN8"
    """GS1 8-digit International Article Number (European Article Number)."""
    EAN13 = "EAN13"
    """GS1 13-digit International Article Number (European Article Number)."""
    DATA_BAR = "DataBar"
    """GS1 DataBar barcode."""
    CODE93 = "Code93"
    """Code 93 barcode, as defined in ANSI/AIM BC5-1995."""
    CODABAR = "Codabar"
    """Codabar barcode, as defined in ANSI/AIM BC3-1995."""
    DATA_BAR_EXPANDED = "DataBarExpanded"
    """GS1 DataBar Expanded barcode."""
    ITF = "ITF"
    """Interleaved 2 of 5 barcode, as defined in ANSI/AIM BC2-1995."""
    MICRO_Q_R_CODE = "MicroQRCode"
    """Micro QR code, as defined in ISO/IEC 23941:2022."""
    AZTEC = "Aztec"
    """Aztec code, as defined in ISO/IEC 24778:2008."""
    DATA_MATRIX = "DataMatrix"
    """Data matrix code, as defined in ISO/IEC 16022:2006."""
    MAXI_CODE = "MaxiCode"
    """MaxiCode, as defined in ISO/IEC 16023:2000."""


class DocumentBuildMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Custom document model build mode."""

    TEMPLATE = "template"
    """Target documents with similar visual templates."""
    NEURAL = "neural"
    """Support documents with diverse visual templates."""


class DocumentFieldType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Semantic data type of the field value."""

    STRING = "string"
    """Plain text."""
    DATE = "date"
    """Date, normalized to ISO 8601 (YYYY-MM-DD) format."""
    TIME = "time"
    """Time, normalized to ISO 8601 (hh:mm:ss) format."""
    PHONE_NUMBER = "phoneNumber"
    """Phone number, normalized to E.164 (+{CountryCode}{SubscriberNumber}) format."""
    NUMBER = "number"
    """Floating point number, normalized to double precision floating point."""
    INTEGER = "integer"
    """Integer number, normalized to 64-bit signed integer."""
    SELECTION_MARK = "selectionMark"
    """Is field selected?"""
    COUNTRY_REGION = "countryRegion"
    """Country/region, normalized to ISO 3166-1 alpha-3 format (ex. USA)."""
    SIGNATURE = "signature"
    """Is signature present?"""
    ARRAY = "array"
    """List of subfields of the same type."""
    OBJECT = "object"
    """Named list of subfields of potentially different types."""
    CURRENCY = "currency"
    """Currency amount with optional currency symbol and unit."""
    ADDRESS = "address"
    """Parsed address."""
    BOOLEAN = "boolean"
    """Boolean value, normalized to true or false."""


class DocumentFormulaKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Formula kind."""

    INLINE = "inline"
    """A formula embedded within the content of a paragraph."""
    DISPLAY = "display"
    """A formula in display mode that takes up an entire line."""


class DocumentSelectionMarkState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the selection mark."""

    SELECTED = "selected"
    """The selection mark is selected, often indicated by a check ✓ or cross X inside
    #: the selection mark."""
    UNSELECTED = "unselected"
    """The selection mark is not selected."""


class DocumentSignatureType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Presence of signature."""

    SIGNED = "signed"
    """A signature is detected."""
    UNSIGNED = "unsigned"
    """No signatures are detected."""


class DocumentTableCellKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Table cell kind."""

    CONTENT = "content"
    """Contains the main content/data."""
    ROW_HEADER = "rowHeader"
    """Describes the content of the row."""
    COLUMN_HEADER = "columnHeader"
    """Describes the content of the column."""
    STUB_HEAD = "stubHead"
    """Describes the row headers, usually located at the top left corner of a table."""
    DESCRIPTION = "description"
    """Describes the content in (parts of) the table."""


class FontStyle(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Font style."""

    NORMAL = "normal"
    """Characters are represented normally."""
    ITALIC = "italic"
    """Characters are visually slanted to the right."""


class FontWeight(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Font weight."""

    NORMAL = "normal"
    """Characters are represented normally."""
    BOLD = "bold"
    """Characters are represented with thicker strokes."""


class LengthUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The unit used by the width, height, and polygon properties. For images, the unit is "pixel".
    For PDF, the unit is "inch".
    """

    PIXEL = "pixel"
    """Length unit for image files."""
    INCH = "inch"
    """Length unit for PDF files."""


class OperationKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of operation."""

    DOCUMENT_MODEL_BUILD = "documentModelBuild"
    """Build a new custom document model."""
    DOCUMENT_MODEL_COMPOSE = "documentModelCompose"
    """Compose a new custom document model from existing models."""
    DOCUMENT_MODEL_COPY_TO = "documentModelCopyTo"
    """Copy an existing document model to potentially a different resource, region, or
    #: subscription."""
    DOCUMENT_CLASSIFIER_BUILD = "documentClassifierBuild"
    """Build a new custom classifier model."""


class OperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operation status."""

    NOT_STARTED = "notStarted"
    """The operation has not started yet."""
    RUNNING = "running"
    """The operation is in progress."""
    FAILED = "failed"
    """The operation has failed."""
    SUCCEEDED = "succeeded"
    """The operation has succeeded."""
    CANCELED = "canceled"
    """The operation has been canceled."""


class ParagraphRole(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Semantic role of the paragraph."""

    PAGE_HEADER = "pageHeader"
    """Text near the top edge of the page."""
    PAGE_FOOTER = "pageFooter"
    """Text near the bottom edge of the page."""
    PAGE_NUMBER = "pageNumber"
    """Page number."""
    TITLE = "title"
    """Top-level title describing the entire document."""
    SECTION_HEADING = "sectionHeading"
    """Sub heading describing a section of the document."""
    FOOTNOTE = "footnote"
    """A note usually placed after the main content on a page."""
    FORMULA_BLOCK = "formulaBlock"
    """A block of formulas, often with shared alignment."""


class SplitMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Document splitting mode."""

    AUTO = "auto"
    """Automatically split file into documents."""
    NONE = "none"
    """Treat the entire file as a single document."""
    PER_PAGE = "perPage"
    """Treat each page in the file as a separate document."""


class StringIndexType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Method used to compute string offset and length."""

    TEXT_ELEMENTS = "textElements"
    """User-perceived display character, or grapheme cluster, as defined by Unicode
    #: 8.0.0."""
    UNICODE_CODE_POINT = "unicodeCodePoint"
    """Character unit represented by a single unicode code point.  Used by Python 3."""
    UTF16_CODE_UNIT = "utf16CodeUnit"
    """Character unit represented by a 16-bit Unicode code unit.  Used by JavaScript,
    #: Java, and .NET."""
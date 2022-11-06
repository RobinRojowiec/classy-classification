from typing import Union

from spacy.language import Language

from .classifiers.classy_spacy import (
    classySpacyExternalFewShot,
    classySpacyExternalFewShotMultiLabel,
    classySpacyInternalFewShot,
    classySpacyInternalFewShotMultiLabel,
)
from .classifiers.sentence_transformer import (
    classySentenceTransformer as classyClassifier,
)
from .classifiers.spacy_external import classySpacyExternalZeroShot

__all__ = [
    "classyClassifier",
    "classySpacyExternalFewShot",
    "classySpacyExternalFewShotMultiLabel",
    "classySpacyExternalZeroShot",
    "classySpacyInternalFewShot",
    "classySpacyInternalFewShotMultiLabel",
]


@Language.factory(
    "text_categorizer",
    default_config={
        "data": None,
        "model": None,
        "device": "cpu",
        "config": None,
        "cat_type": "few",
        "multi_label": False,
        "include_doc": True,
        "include_sent": False,
    },
)
def make_text_categorizer(
    nlp: Language,
    name: str,
    data: Union[dict, list],
    device: str,
    config: dict = None,
    model: str = None,
    cat_type: str = "few",
    multi_label: bool = False,
    include_doc: bool = True,
    include_sent: bool = False,
):
    if model == "spacy":
        if cat_type == "zero":
            raise NotImplementedError("Cannot use spacy internal embeddings with zero-shot classification")
        if multi_label:
            return classySpacyInternalFewShotMultiLabel(
                nlp=nlp,
                name=name,
                data=data,
                config=config,
                include_doc=include_doc,
                include_sent=include_sent,
            )
        else:
            return classySpacyInternalFewShot(
                nlp=nlp,
                name=name,
                data=data,
                config=config,
                include_doc=include_doc,
                include_sent=include_sent,
            )
    else:
        if cat_type == "zero":
            if model:
                return classySpacyExternalZeroShot(
                    nlp=nlp,
                    name=name,
                    data=data,
                    device=device,
                    model=model,
                    include_doc=include_doc,
                    include_sent=include_sent,
                )
            else:
                return classySpacyExternalZeroShot(
                    nlp=nlp,
                    name=name,
                    data=data,
                    device=device,
                    include_doc=include_doc,
                    include_sent=include_sent,
                )
        if multi_label:
            if model:
                return classySpacyExternalFewShotMultiLabel(
                    nlp=nlp,
                    name=name,
                    data=data,
                    device=device,
                    model=model,
                    include_doc=include_doc,
                    include_sent=include_sent,
                )
            else:
                return classySpacyExternalFewShotMultiLabel(
                    nlp=nlp,
                    name=name,
                    data=data,
                    device=device,
                    include_doc=include_doc,
                    include_sent=include_sent,
                )
        else:
            if model:
                return classySpacyExternalFewShot(
                    nlp=nlp,
                    name=name,
                    data=data,
                    device=device,
                    model=model,
                    config=config,
                    include_doc=include_doc,
                    include_sent=include_sent,
                )
            else:
                return classySpacyExternalFewShot(
                    nlp=nlp,
                    name=name,
                    data=data,
                    device=device,
                    config=config,
                    include_doc=include_doc,
                    include_sent=include_sent,
                )

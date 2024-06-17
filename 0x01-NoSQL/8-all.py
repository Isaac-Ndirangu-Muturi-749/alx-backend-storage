#!/usr/bin/env python3
"""
Module 8-all
"""

def list_all(mongo_collection):
    """
    List all documents in a collection

    :param mongo_collection: The pymongo collection object
    :return: A list of documents, or an empty list if no documents are found
    """
    if mongo_collection is None:
        return []

    documents = list(mongo_collection.find())
    return documents

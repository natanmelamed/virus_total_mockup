def pop_irrelevant_relationships(relationships_list: str, relationships_data: dict) -> dict:
    relationships_list: list = relationships_list.split(",")
    for current_relationship in list(relationships_data["data"]["relationships"]):
        if current_relationship not in relationships_list:
            relationships_data["data"]["relationships"].pop(current_relationship)
    return relationships_data

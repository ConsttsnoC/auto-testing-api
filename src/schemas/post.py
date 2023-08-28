POST_SCHEMA = {
    "type": "object",
    "properties": {
        "company_id": {"type": "number"},
        "company_name": {"type": "string"},
        "company_address": {"type": "string"},
        "company_status": {"type": "string"}
    },
    "required": ["company_id"]
}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Rule Configuration API")

class RuleConfigRequest(BaseModel):
    rule_name: str
    db_name: str
    dataset_name: str
    column_name: str
    rule_type: str
    baseline_value: float
    threshold_value: float

@app.post("/configure-rule", summary="Configure a new rule")
def configure_rule(payload: RuleConfigRequest):
    print(f"Configuring rule: {payload}")
    return {
        "message": f"{payload.rule_name} is configured successfully"
    }

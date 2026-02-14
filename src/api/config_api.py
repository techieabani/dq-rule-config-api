from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from src.utils.logger import setup_logger

logger = setup_logger("DQ_RULE_CONFIG_API")

app = FastAPI(title="Rule Configuration API")

# -------------------------
# Models
# -------------------------

class AttributeRuleInfo(BaseModel):
    baseline_value: Optional[float] = None
    threshold_value: Optional[float] = None
    
class AttributeInfo(BaseModel):
    column_name: str
    rule_type: str
    baseline_source: str
    rule_details: AttributeRuleInfo
    
class RuleConfigRequest(BaseModel):
    rule_name: str
    db_name: str
    dataset_name: str
    connectivity_id: str
    attributes: list[AttributeInfo]

# ----------------------------
# POST API to configure a rule
# ----------------------------

@app.post("/api/dq/config/v1/rules", status_code=201, summary="Configure a new data quality rule")
def configure_rule(payload: RuleConfigRequest):
    logger.info(f"Configuring data quality rule: {payload}")
    return {
        "message": f"Rule '{payload.rule_name}' is configured successfully"
    }

# -------------------------
# Hardcoded repository list
# -------------------------
REPO_CONNECTIVITY = [
    {"repository_name": "AWSRepo", "connectivity_id": "1"},
    {"repository_name": "DatabricksRepo", "connectivity_id": "2"},
    {"repository_name": "KubernetesRepo", "connectivity_id": "3"}
]

# ------------------------------------------------------
# GET API to retrieve connectivity id by repository name
# ------------------------------------------------------
@app.get(
    "/api/dq/config/v1/repositories/{repo_name}/connectivity",
    summary="Get connectivity id for a repository"
)
def get_connectivity_id_by_repo_name(repo_name: str):
    logger.info(f"Fetching connectivity ID for repo: {repo_name}")

    for repo in REPO_CONNECTIVITY:
        if repo["repository_name"].lower() == repo_name.lower():
            return {
                "connectivity_id": repo["connectivity_id"]
            }

    logger.error(f"Repository not found: {repo_name}")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The provided repo '{repo_name}' doesn't exist"
    )
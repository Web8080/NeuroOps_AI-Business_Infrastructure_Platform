from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/")
def list_dashboards():
    raise HTTPException(501, "Not implemented")


@router.get("/{dashboard_id}")
def get_dashboard(dashboard_id: str):
    raise HTTPException(501, "Not implemented")


@router.get("/{dashboard_id}/widgets")
def get_widgets(dashboard_id: str):
    raise HTTPException(501, "Not implemented")

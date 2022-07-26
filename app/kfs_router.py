from fastapi import APIRouter, Query
from pydantic import BaseModel, Field

from .kfs import calculator

router = APIRouter(
    prefix="/calculator",
    tags=["calculation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"Location": "The Calculation Router"}


@router.get("/assessmentQuick")
async def read_user_item(
    arv: int = Query(default=0, ge=0, description="After Repair Value"),
    pp: int = Query(default=0, ge=0, description="Purchase Price"),
    rc: int = Query(default=0, ge=0, description="Repair Costs"),
):
    item = {"arv": arv, "pp": pp, "rc": rc}
    result = calculator.calc_assessment_quick(arv, pp, rc)
    item.update(result)
    return item


# class assessment_quick(BaseModel):
#     arv: float = Field(default=0, title="After Repair Value")
#     pp: float = Field(default=0, title="Purchase Price")
#     rc: float = Field(default=0, title="Total Repair Costs")


# @router.post(
#     "/assessmentQuick",
#     summary="Quick Assessment",
# )
# async def calculate_assessment_quick(item: assessment_quick):
#     result = calculator.calc_assessment_quick(item.arv, item.pp, item.rc)
#     return result

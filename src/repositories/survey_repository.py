import pandas as pd
from sqlalchemy import text

from src.constants import QUESTION_COLUMNS
from src.db import get_engine


def create_submission(respondent: dict, answers: dict) -> int:
    respondent_query = text(
        """
        INSERT INTO respondents
            (gender, age, work_unit, position_name, education, years_of_service)
        VALUES
            (:gender, :age, :work_unit, :position_name, :education, :years_of_service)
        """
    )
    answer_columns = ", ".join(QUESTION_COLUMNS)
    answer_values = ", ".join(f":{column}" for column in QUESTION_COLUMNS)
    questionnaire_query = text(
        f"""
        INSERT INTO questionnaires (respondent_id, {answer_columns})
        VALUES (:respondent_id, {answer_values})
        """
    )

    with get_engine().begin() as conn:
        result = conn.execute(respondent_query, respondent)
        respondent_id = result.lastrowid
        conn.execute(questionnaire_query, {"respondent_id": respondent_id, **answers})
        return respondent_id


def get_respondents(filters: dict | None = None) -> pd.DataFrame:
    filters = filters or {}
    conditions = []
    params = {}

    if filters.get("gender") and filters["gender"] != "Semua":
        conditions.append("gender = :gender")
        params["gender"] = filters["gender"]
    if filters.get("work_unit"):
        conditions.append("work_unit LIKE :work_unit")
        params["work_unit"] = f"%{filters['work_unit']}%"
    if filters.get("start_date"):
        conditions.append("DATE(created_at) >= :start_date")
        params["start_date"] = filters["start_date"]
    if filters.get("end_date"):
        conditions.append("DATE(created_at) <= :end_date")
        params["end_date"] = filters["end_date"]

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    query = f"""
        SELECT
            id,
            gender,
            age,
            work_unit,
            position_name,
            education,
            years_of_service,
            created_at,
            updated_at
        FROM respondents
        {where_clause}
        ORDER BY created_at DESC
    """
    return pd.read_sql(text(query), get_engine(), params=params)


def get_questionnaires(filters: dict | None = None) -> pd.DataFrame:
    filters = filters or {}
    conditions = []
    params = {}

    if filters.get("gender") and filters["gender"] != "Semua":
        conditions.append("r.gender = :gender")
        params["gender"] = filters["gender"]
    if filters.get("work_unit"):
        conditions.append("r.work_unit LIKE :work_unit")
        params["work_unit"] = f"%{filters['work_unit']}%"
    if filters.get("start_date"):
        conditions.append("DATE(q.submitted_at) >= :start_date")
        params["start_date"] = filters["start_date"]
    if filters.get("end_date"):
        conditions.append("DATE(q.submitted_at) <= :end_date")
        params["end_date"] = filters["end_date"]

    where_clause = f"WHERE {' AND '.join(conditions)}" if conditions else ""
    query = f"""
        SELECT
            q.id AS questionnaire_id,
            r.id AS respondent_id,
            r.gender,
            r.age,
            r.work_unit,
            r.position_name,
            r.education,
            r.years_of_service,
            q.{", q.".join(QUESTION_COLUMNS)},
            ROUND((q.PEOU1 + q.PEOU2 + q.PEOU3 + q.PEOU4 + q.PEOU5 + q.PEOU6 + q.PEOU7) / 7, 2) AS peou_avg,
            ROUND((q.PU1 + q.PU2 + q.PU3 + q.PU4 + q.PU5 + q.PU6 + q.PU7) / 7, 2) AS pu_avg,
            ROUND((q.BI1 + q.BI2 + q.BI3 + q.BI4 + q.BI5 + q.BI6) / 6, 2) AS bi_avg,
            q.submitted_at
        FROM questionnaires q
        JOIN respondents r ON r.id = q.respondent_id
        {where_clause}
        ORDER BY q.submitted_at DESC
    """
    return pd.read_sql(text(query), get_engine(), params=params)


def update_respondent(respondent_id: int, data: dict) -> None:
    query = text(
        """
        UPDATE respondents SET
            gender = :gender,
            age = :age,
            work_unit = :work_unit,
            position_name = :position_name,
            education = :education,
            years_of_service = :years_of_service
        WHERE id = :id
        """
    )
    with get_engine().begin() as conn:
        conn.execute(query, {"id": respondent_id, **data})


def delete_respondent(respondent_id: int) -> None:
    with get_engine().begin() as conn:
        conn.execute(text("DELETE FROM respondents WHERE id = :id"), {"id": respondent_id})

"""Pydantic request/response models."""
from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    # FIX: Enforce non-empty strings
    org_name: str = Field(..., min_length=1)
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)


class LoginRequest(BaseModel):
    # FIX: Enforce non-empty strings
    org_name: str = Field(..., min_length=1)
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)


class RefreshRequest(BaseModel):
    # FIX: Enforce non-empty string
    refresh_token: str = Field(..., min_length=1)


class RoomCreateRequest(BaseModel):
    # FIX: Enforce non-empty string, positive capacity, and non-negative rate
    name: str = Field(..., min_length=1)
    capacity: int = Field(..., gt=0)
    hourly_rate_cents: int = Field(..., ge=0)


class BookingCreateRequest(BaseModel):
    # FIX: Enforce positive room ID
    room_id: int = Field(..., gt=0)
    start_time: str
    end_time: str
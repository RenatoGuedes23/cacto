#!/usr/bin/python
# -*- encoding: utf-8 -*-

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database.base_db import Base


class User(Base):
    __tablename__ = "tb_user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


    
class Setting(Base):
    __tablename__ = "tb_setting"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    created = Column(DateTime)
    is_active = Column(Boolean, default=True)

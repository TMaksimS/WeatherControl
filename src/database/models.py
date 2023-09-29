from sqlalchemy import String, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class City(Base):
    __tablename__ = 'cities'
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True,
    )
    name: Mapped[str] = mapped_column(
        String(100), nullable=False, name="Название города"
    )
    country: Mapped[str] = mapped_column(
        String(5), nullable=True, name="Абривиатура страны"
    )
    lat: Mapped[float] = mapped_column(
        Float(),
        nullable=False,
        name="Широта"
    )
    lon: Mapped[float] = mapped_column(
        Float(),
        nullable=False,
        name="Долгота"
    )
    city_weather: Mapped["Weather"] = relationship(
        uselist=False,
        back_populates="city",
        lazy=False
    )


class Weather(Base):
    __tablename__ = "weather"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True,
    )
    type: Mapped[str] = mapped_column(
        String(100), nullable=False, name="Тип погоды"
    )
    temp: Mapped[float] = mapped_column(
        Float(), nullable=False, name="Температура в *C"
    )
    feels_like: Mapped[float] = mapped_column(
        Float(), nullable=False, name="Ощущается как"
    )
    wind_speed: Mapped[float] = mapped_column(
        Float(), nullable=False, name="Скорость ветра"
    )
    description: Mapped[str] = mapped_column(
        String(225), nullable=True, name="Описание погоды"
    )
    city_id: Mapped[int] = mapped_column(ForeignKey(column="cities.id", ondelete="CASCADE"))
    city: Mapped["City"] = relationship(back_populates="city_weather")

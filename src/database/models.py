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
    city_weather: Mapped["Weather"] = relationship(
        uselist=False,
        back_populates="city",
        # sa_relationship_kwargs={'lazy': 'joined'},
        lazy=False
    )


class Weather(Base):
    __tablename__ = "weather"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True,
    )
    temp: Mapped[float] = mapped_column(
        Float(), nullable=False, name="Температура в *C"
    )
    description: Mapped[str] = mapped_column(
        String(225), nullable=True, name="Описание погоды"
    )
    city_id: Mapped[int] = mapped_column(ForeignKey(column="cities.id", ondelete="CASCADE"))
    city: Mapped["City"] = relationship(back_populates="city_weather")

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
    String(120), unique=True, nullable=False)
    subscription_date: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=False)

    # relacion de favoritos
    favorites: Mapped[list["Favorite"]] = db.relationship(
        "Favorite", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "subscription_date": self.subscription_date,
        }
class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    gender: Mapped[str] = mapped_column(String(20))
    birth_year: Mapped[str] = mapped_column(String(10))
    description: Mapped[str] = mapped_column(String(250))

    # RELACIÓN con favoritos 
    favorites: Mapped[list["Favorite"]] = db.relationship(
        "Favorite", back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "description": self.description
        }
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped[str] = mapped_column(String(50))
    terrain: Mapped[str] = mapped_column(String(50))
    population: Mapped[str] = mapped_column(String(50))

    # Relación con favoritos
    favorites: Mapped[list["Favorite"]] = db.relationship("Favorite", back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population
        }
class Vehicle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    speed: Mapped[str] = mapped_column(String(50))
    color: Mapped[str] = mapped_column(String(50))
    model_type: Mapped[str] = mapped_column(String(100))

    # Relación con favoritos
    favorites: Mapped[list["Favorite"]] = db.relationship("Favorite", back_populates="vehicle")

    def serialize(self):
        return {
            "id": self.id,
            "speed": self.speed,
            "color": self.color,
            "model_type": self.model_type
        }
class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # Clave foránea a User
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    user: Mapped["User"] = db.relationship("User", back_populates="favorites")

    # Clave foránea a Character (opcional)
    character_id: Mapped[int] = mapped_column(db.ForeignKey("character.id"), nullable=True)
    character: Mapped["Character"] = db.relationship("Character", back_populates="favorites")

    # Clave foránea a Planet (opcional)
    planet_id: Mapped[int] = mapped_column(db.ForeignKey("planet.id"), nullable=True)
    planet: Mapped["Planet"] = db.relationship("Planet", back_populates="favorites")

    # Clave foránea a Vehicle (opcional)
    vehicle_id: Mapped[int] = mapped_column(db.ForeignKey("vehicle.id"), nullable=True)
    vehicle: Mapped["Vehicle"] = db.relationship("Vehicle", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }


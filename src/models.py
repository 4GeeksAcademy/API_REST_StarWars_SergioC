from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import ForeignKey

db = SQLAlchemy()


class User(db.Model):
  __tablename__ = "user"

  id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
  email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
  password: Mapped[str] = mapped_column(nullable=False)

  # relationships
  favorites: Mapped[List["Favorites"]] = relationship(back_populates="user")

  def user_information(self):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email,
      "password": self.password,
    }

class Favorites(db.Model):
  __tablename__ = "favorites"

  id: Mapped[int] = mapped_column(primary_key=True)

  # foreingkeys
  user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
  
  # relationships
  user: Mapped["User"] = relationship(back_populates="favorites")
  favorites_planet: Mapped[List["FavoritePlanet"]] = relationship(back_populates="favorites")
  favorites_character: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="favorites")
  favorites_starship: Mapped[List["FavoriteStarship"]] = relationship(back_populates="favorites")

  
  
class FavoritePlanet(db.Model):
  __tablename__ = "favorite_planet"
    
  id: Mapped[int] = mapped_column(primary_key=True)
    
  # foreingkeys
  favorites_id: Mapped[int] = mapped_column(ForeignKey("favorites.id"), nullable=False)
  planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)
    
  # relationships
  favorites: Mapped["Favorites"] = relationship(back_populates="favorites_planet")
  planet: Mapped["Planet"] = relationship(back_populates="favorites_planet")


    
class FavoriteCharacter(db.Model):
  __tablename__ = "favorite_character"
      
  id: Mapped[int] = mapped_column(primary_key=True)
      
  # foreinkeys
  favorites_id: Mapped[int] = mapped_column(ForeignKey("favorites.id"), nullable=False)
  character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=False)
      
  # relationships
  favorites: Mapped["Favorites"] = relationship(back_populates="favorites_character")
  character: Mapped["Character"] = relationship(back_populates="favorites_character")


  
class FavoriteStarship(db.Model):
  __tablename__ = "favorite_starship"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  
  # foreingkeys
  favorites_id: Mapped[int] = mapped_column(ForeignKey("favorites.id"), nullable=False)
  starship_id: Mapped[int] = mapped_column(ForeignKey("starship.id"), nullable=False)
  
  # relationships
  favorites: Mapped["Favorites"] = relationship(back_populates="favorites_starship")
  starship: Mapped["Starship"] = relationship(back_populates="favorites_starship")



  
class Planet(db.Model):
  __tablename__= "planet"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
  climate: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
  diameter: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
  
  # relationships
  characters: Mapped[List["Character"]] = relationship(back_populates="planet")
  favorites_planet: Mapped[List["FavoritePlanet"]] = relationship(back_populates="planet")

  def planet_informacion(self):
    return {
      "id": self.id,
      "name": self.name,
      "climate": self.climate,
      "diameter": self.diameter,
    }



class Character(db.Model):
  __tablename__= "character"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(20), unique=False, nullable=False)
  lastname: Mapped[str] = mapped_column(String(90), unique=False, nullable=False)
  height: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
  
  # foreingkeys
  planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=False)
  
  # relationships
  planet: Mapped["Planet"] = relationship(back_populates="characters")
  favorites_character: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="character")


  def mostrar_informacion(self):
    return {
      "id": self.id,
      "name": self.name,
      "lastname": self.lastname,
      "height": self.height,
      "planet_id": self.planet_id,
    }

  

class Starship(db.Model):
  __tablename__= "starship"
  
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
  crew: Mapped[int] = mapped_column(Integer, unique=False, nullable=False)
  manufacturer: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

  #relationship
  favorites_starship: Mapped[List["FavoriteStarship"]] = relationship(back_populates="starship")

  def starship_informacion(self):
    return {
      "id": self.id,
      "name": self.name,
      "crew": self.crew,
      "manufacturer": self.manufacturer,
    }
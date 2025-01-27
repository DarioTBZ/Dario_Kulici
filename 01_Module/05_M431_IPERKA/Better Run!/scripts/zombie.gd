extends CharacterBody2D

class_name zombie

@export_group("Locomotion")
@export var rotation_speed: float = 2
@export var wandering_speed = 150
@export var navigation_target: Node2D
@export var chasing_speed = 200

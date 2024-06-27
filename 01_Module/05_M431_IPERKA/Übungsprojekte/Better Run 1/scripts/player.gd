extends CharacterBody2D

# signals
signal player_fired_bullet


@export var max_speed = 250
@export var acceleration = 1200
var friction = 2000
@export var player_ui: PlayerUI

@onready var axis = Vector2.ZERO

@onready var end_of_gun = $End_Of_Gun
@onready var gun_direction = $Gun_Direction
@onready var health_system = $HealthSystem as HealthSystem

func _ready():
	
	player_ui.set_life_bar_max_value(health_system.base_health)

func _physics_process(delta):
	# Shoot
	if Input.is_action_just_released("shoot"):
		shoot()
	
	look_at(get_global_mouse_position())
	# Movement
	move(delta)
	
func get_input_axis():
	axis.x = int(Input.is_action_pressed("right")) - int(Input.is_action_pressed("left"))
	axis.y = int(Input.is_action_pressed("down")) - int(Input.is_action_pressed("up"))
	return axis.normalized()
	
func move(delta):
	axis = get_input_axis()
	
	if axis == Vector2.ZERO:
		apply_friction(friction * delta)
		
	else: 
		apply_movement(axis * acceleration * delta) 
	
	move_and_slide()
	
func apply_friction(amount):
	velocity = Vector2.ZERO
		
func apply_movement(accel):
	velocity += accel
	velocity = velocity.limit_length(max_speed)
	
func shoot():
	var bullet_instance = preload("res://scenes/bullet.tscn").instantiate()
	var direction = (gun_direction.global_position - end_of_gun.global_position).normalized()
	emit_signal("player_fired_bullet", bullet_instance, end_of_gun.global_position, direction)

func take_damage(damage: int):
	health_system.take_damage(damage)
	player_ui.update_life_bar_value(health_system.current_health)

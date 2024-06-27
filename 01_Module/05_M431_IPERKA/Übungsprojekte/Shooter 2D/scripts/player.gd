extends CharacterBody2D

signal player_fired_bullet(bullet, position, direction)

# Exported to a menu 
@export var speed = 15000
@export var Bullet: PackedScene

# Gets called when game is started
@onready var end_of_gun = $EndOfGun
@onready var gun_direction = $GunDirection


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Direction
	var movement_direction := Vector2.ZERO
	
	
	if Input.is_action_pressed("up"):
		movement_direction.y = -1
	if Input.is_action_pressed("down"):
		movement_direction.y = 1
	if Input.is_action_pressed("left"):
		movement_direction.x = -1
	if Input.is_action_pressed("right"):
		movement_direction.x = 1
		
	movement_direction = movement_direction.normalized()
	
	velocity = movement_direction * speed * delta
	
	move_and_slide()

	look_at(get_global_mouse_position())
	


func _unhandled_input(event):
	if event.is_action_released("shoot"):
		shoot()
		
		
		
func shoot():
	var bullet_instance = preload("res://scenes/bullet.tscn").instantiate()
	var direction = (gun_direction.global_position - end_of_gun.global_position).normalized()
	emit_signal("player_fired_bullet", bullet_instance, end_of_gun.global_position, direction)

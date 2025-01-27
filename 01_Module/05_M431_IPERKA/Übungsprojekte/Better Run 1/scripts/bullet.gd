extends Area2D

@export var speed = 20

@onready var kill_timer = $Kill_Timer

var direction := Vector2.ZERO

func _ready():
	kill_timer.start()
	
func _physics_process(delta):
	if direction != Vector2.ZERO:
		var velocity = direction * speed
		global_position += velocity

func set_direction(direction: Vector2):
	self.direction = direction
	rotation += direction.angle()
	
func Kill_Bullet_on_Timeout():
	queue_free()

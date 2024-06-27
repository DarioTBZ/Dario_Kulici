extends Area2D
class_name Bullet

@export var speed = 20

@onready var kill_timer = $KillTimer

var direction := Vector2.ZERO

func _ready():
	kill_timer.start()

func _physics_process(_delta):
	if direction != Vector2.ZERO:
		var velocity = direction * speed
		global_position += velocity


func set_direction(direction: Vector2):
	self.direction = direction
	rotation += direction.angle()


func _on_kill_timer_timeout():
	queue_free()

extends Control

func play_button_pressed():
	get_tree().change_scene_to_file("res://scenes/game.tscn")


func settings_button_pressed():
	pass # Replace with function body.


func quit_button_pressed():
	get_tree().quit()


func _on_stash_pressed():
	get_tree().change_scene_to_file("res://scenes/stash.tscn")

--Funciona em conjunto com changePosition1
function changePosition2()
	game.Workspace.Part.Position = Vector3.new(21, 0.5, 19)
end
game.Workspace.ButtonRed.Touched:Connect(changePosition2)
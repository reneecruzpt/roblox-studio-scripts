--Funciona em conjunto com changePosition2
function changePosition1()
	game.Workspace.Part.Position = Vector3.new(21, 0.5, -9)
end
game.Workspace.ButtonGreen.Touched:Connect(changePosition1)
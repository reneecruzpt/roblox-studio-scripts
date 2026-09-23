function lightOn()
	game.Workspace.Light.SpotLight.Enabled = true
end
game.Workspace.Part.Touched:Connect(lightOn)
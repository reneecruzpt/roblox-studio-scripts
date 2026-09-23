function changeMaterial()
    game.Workspace.Part.Transparency = 0.5
end
game.Workspace.Part.Touched:Connect(changeMaterial)
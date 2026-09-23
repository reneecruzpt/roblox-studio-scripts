function changeMaterial()
    game.Workspace.Part.Material = Enum.Material.Neon
end
game.Workspace.Part.Touched:Connect(changeMaterial)
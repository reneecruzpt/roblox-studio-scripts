function changeColor()
    game.Workspace.Part.BrickColor = BrickColor.new('Lime green')
end
game.Workspace.Part.Touched:Connect(changeColor)
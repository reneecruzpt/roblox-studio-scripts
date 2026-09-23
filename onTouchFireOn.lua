function onTouch(who)
    game.Workspace.Part.Fire.Enabled = true
end
game.workspace.AreaPart.Touched:Connect(onTouch)
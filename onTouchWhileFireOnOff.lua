function onTouch(who)
    game.Workspace.Part.Fire.Enabled = true
end
function onTouchEnded(who)
    wait(3)
    game.Workspace.Part.Fire.Enabled = false
end
game.workspace.AreaPart.Touched:Connect(onTouch)
game.workspace.AreaPart.TouchEnded:Connect(onTouchEnded)
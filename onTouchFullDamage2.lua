function onTouchDamage2(who)
    who.Parent.Humanoid.Health=0
end
game.workspace.Part.Touched:Connect(onTouchDamage2)
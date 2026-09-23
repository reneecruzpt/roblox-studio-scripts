function onTouchDamage(who)
	if who.Parent.Humanoid then
		who.Parent.Humanoid.Health = 0
	end
end
game.Workspace.Part.Touched:Connect(onTouchDamage)
function onTouchDestroy(who)
	game.Workspace.Part:Destroy()
end
game.Workspace.Part.Touched:Connect(onTouchDestroy)
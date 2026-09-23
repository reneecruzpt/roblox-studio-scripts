B=0
while true do	
	game.Lighting.ClockTime=B
	B=B+0.1
	if B>24 then B=0 end
	if B > 20 then workspace.Part.Transparency=1 end
	if B < 6 then workspace.Part.Transparency=1 end
	if B > 6 and B < 16 then workspace.Part.Transparency=0  end
	wait()
end
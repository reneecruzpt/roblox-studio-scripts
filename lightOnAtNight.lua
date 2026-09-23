B=0
while true do game.Lighting.ClockTime=B
    B=B+0.1
    if B > 24 then B=0 end
    if B > 16 then game.workspace.Part.SpotLight.Enabled = true end
    if B < 6 then game.workspace.Part.SpotLight.Enabled = true end
    if B > 6 and B < 16 then game.workspace.Part.SpotLight.Enabled = false end
    wait()
end
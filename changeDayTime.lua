B=0
while true do
    game.Lighting.ClockTime=B
    B = B+0.1
    if B > 24 then B = 0 end
    wait()
end
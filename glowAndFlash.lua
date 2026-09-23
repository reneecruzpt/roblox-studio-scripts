while true do
    game.workspace.Part1.PointLight.Enabled = false
    game.workspace.Part2.SpotLight.Enabled = false
    game.workspace.Part3.SurfaceLight.Enabled = false
    wait(1)
    game.workspace.Part1.PointLight.Enabled = true
    game.workspace.Part2.SpotLight.Enabled = true
    game.workspace.Part3.SurfaceLight.Enabled = true
    wait(1)
end
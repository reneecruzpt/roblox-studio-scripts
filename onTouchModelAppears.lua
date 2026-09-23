--O Script deve ser adicionado a ServerScript Service
--O modelo deve estar em ServerStorage
function onTouchPart(who)
    game.ServerStorage.Model.Parent=game.Workspace
end
game.workspace.Part.Touched:Connect(onTouchPart) --a parte deve ser na parte a ser tocada para o modelo aparecer-
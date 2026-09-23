--O Script deve ser adicionado a ServerScript Service
game.workspace.Model.Parent=game.ServerStorage --Envia o modelo para ServerStorage
function onTouchPart(who)
    game.ServerStorage.Model.Parent=game.Workspace
end
game.workspace.Part.Touched:Connect(onTouchPart) --a parte deve ser uma das partes do modelo a que será tocada-
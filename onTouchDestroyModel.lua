print("O script está sendo executado.")

-- Verifica se o modelo existe no Workspace
local model = game.Workspace:FindFirstChild("Model")

if model then
    print("Modelo encontrado no Workspace: " .. model.Name)

    local function onModelTouched(part)
        -- Verifica se a parte que tocou não é descendente do modelo
        if part:IsDescendantOf(model) then return end
        print(model:GetFullName() .. " foi tocado por " .. part:GetFullName())
        -- Destroi o modelo
        model:Destroy()
    end

    -- Conecta o evento Touched a todas as partes do modelo (BasePart)
    for _, child in ipairs(model:GetDescendants()) do
        if child:IsA("BasePart") then
            child.Touched:Connect(onModelTouched)
            print("Evento Touched conectado à parte: " .. child.Name)
        end
    end
else
    print("Modelo não encontrado no Workspace.")
end

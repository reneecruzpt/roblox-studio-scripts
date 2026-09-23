local fire_on = true

function onTouchDamage(who)
    if fire_on == true and who.Parent.Humanoid then
        fire_on = false
        if script.Parent.Fire then
            who.Parent.Humanoid:TakeDamage(20)
            wait(0.2)
            fire_on = true
        end
    end
end

script.Parent.Touched:Connect(onTouchDamage)
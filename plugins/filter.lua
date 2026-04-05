-- AIP-HSD Lua Plugin System
-- Lightweight logic for real-time telemetry filtering.

function filter_event(event_type, severity)
    print("AIP-HSD Lua Filter: Processing " .. event_type .. " (" .. severity .. ")")
    if severity == "LOW" then
        return false -- Filter out low severity
    end
    return true -- Keep others
end

print("Lua Plugin Loaded.")
print("Filter Result (HIGH): ", filter_event("ALERT", "HIGH"))

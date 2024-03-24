// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common_func.emevd N:\GR\data\Param\event\common_macro.emevd      
// @linked    [0,82]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    InitializeEvent(0, 10010000, 0);
    InitializeEvent(0, 10010010, 0);
    InitializeEvent(0, 10010020, 0);
    InitializeEvent(0, 10010040, 0);
    InitializeEvent(0, 10010041, 0);
});

$Event(50, Default, function() {
    
});

// Setup
$Event(10010000, Restart, function() {
    SetCurrentTime(0, 0, 0, false, false, false, 0, 0, 0);
    SetPlayerRespawnPoint(10012020);
    SaveRequest();
});

// Reset Progression
$Event(10010010, Restart, function() {
    BatchSetEventFlags(1047590100, 1047590120, OFF); // Dungeon Progression
    BatchSetEventFlags(1047590200, 1047590220, OFF); // Triggers
    BatchSetEventFlags(1047590300, 1047590320, OFF); // Dungeon Level Scaling
});

// Initial Warp for first spawn when walking towards statue
$Event(10010020, Restart, function() {
    // DEBUG: Temp until class stuff is done
    EndIf(EventFlag(1047610005));
    WaitFor(InArea(10000, 10012510, 1));
    FadeToBlack(1.0, 2.0, true, 0);
    SetEventFlag(0, 1047610005, ON);
    WaitFixedTimeSeconds(1.0);
    SetEventFlag(0, 1047610010, ON);
});

// Apply Rebirth 
$Event(10010040, Restart, function() {
    SetEventFlag(0, 1047610020, OFF); // Reset on reloads
    
    WaitFor(EventFlag(1047610020));
    
    // Warp to Trial of Champions
    FadeToBlack(1.0, 2.0, true, 0);
    SetEventFlag(0, 1047610005, ON);
    WaitFixedTimeSeconds(1.0);
    SetEventFlag(0, 1047610010, ON);
});

// Set Rebirth Options
$Event(10010041, Default, function() {
    BatchSetEventFlags(1047610150, 1047610159, OFF); // Display
    BatchSetEventFlags(1047610200, 1047610209, OFF); // Chosen
    
    InitializeEvent(0, 10010042, 0); // Class 1
    InitializeEvent(1, 10010042, 0); // Class 2
    InitializeEvent(2, 10010042, 0); // Class 3
});

// Set Random Class
$Event(10010042, Default, function() {
    BatchSetEventFlags(1047620000, 1047620009, OFF);
    RandomlySetEventFlagInRange(1047620000, 1047620009, ON);
    
    // First Cascade
    if(EventFlag(1047620000))
    {
        if(!EventFlag(1047610150))
        {
            SetEventFlag(0, 1047610150, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620001, ON);
        }
    }
    
    if(EventFlag(1047620001))
    {
        if(!EventFlag(1047610151))
        {
            SetEventFlag(0, 1047610151, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620002, ON);
        }
    }
    
    if(EventFlag(1047620002))
    {
        if(!EventFlag(1047610152))
        {
            SetEventFlag(0, 1047610152, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620003, ON);
        }
    }
    
    if(EventFlag(1047620003))
    {
        if(!EventFlag(1047610153))
        {
            SetEventFlag(0, 1047610153, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620004, ON);
        }
    }
    
    if(EventFlag(1047620004))
    {
        if(!EventFlag(1047610154))
        {
            SetEventFlag(0, 1047610154, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620005, ON);
        }
    }
    
    if(EventFlag(1047620005))
    {
        if(!EventFlag(1047610155))
        {
            SetEventFlag(0, 1047610155, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620006, ON);
        }
    }
    
    if(EventFlag(1047620006))
    {
        if(!EventFlag(1047610156))
        {
            SetEventFlag(0, 1047610156, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620007, ON);
        }
    }
    
    if(EventFlag(1047620007))
    {
        if(!EventFlag(1047610157))
        {
            SetEventFlag(0, 1047610157, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620008, ON);
        }
    }
    
    if(EventFlag(1047620008))
    {
        if(!EventFlag(1047610158))
        {
            SetEventFlag(0, 1047610158, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620009, ON);
        }
    }
    
    if(EventFlag(1047620009))
    {
        if(!EventFlag(1047610159))
        {
            SetEventFlag(0, 1047610159, ON);
        }
        else
        {
            // Go to the next check
            SetEventFlag(0, 1047620000, ON);
        }
    }
});


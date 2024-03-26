// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common_func.emevd N:\GR\data\Param\event\common_macro.emevd      
// @linked    [0,82]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    InitializeCommonEvent(0, 98006001, 0); // Reset Progression
    InitializeEvent(0, 10010000, 0); // Setup
    InitializeEvent(0, 10010002, 0); // Enter Dungeon
    InitializeEvent(0, 10010003, 0); // Rebirth Options
    InitializeEvent(0, 10010010, 0); // Rebirth Change
    InitializeEvent(0, 10010020, 0); // Blacksmith
    InitializeEvent(0, 10010030, 0); // Enchantress
    
    // Class Previews
    InitializeEvent(0, 10010005, 7010, 10010851, 600100); // Wretch
});

$Event(50, Default, function() {
    
});

// Setup
$Event(10010000, Restart, function() {
    SetCurrentTime(0, 0, 0, false, false, false, 0, 0, 0);
    SetPlayerRespawnPoint(10012020);
    SaveRequest();
});

// Enter Dungeon
$Event(10010002, Restart, function() {
    SetEventFlag(0, 1047610020, OFF); // Reset on reloads
    
    WaitFor(EventFlag(1047610020));
    
    // Change to new Successor
    ForceAnimationPlayback(10000, 60100, true, false, true, 0, 1);
    
    FadeToBlack(0, 1.0, true, 0);
    WaitFixedTimeSeconds(0.5);
    SetEventFlag(0, 1047610021, ON);
    WaitFixedTimeSeconds(0.2);
    
    InitializeCommonEvent(0, 98006000, 0); // Level Warp
    
});

// Set Rebirth Options
$Event(10010003, Default, function() {
    BatchSetEventFlags(1047610150, 1047610159, OFF); // Display
    BatchSetEventFlags(1047610200, 1047610209, OFF); // Chosen
    
    InitializeEvent(0, 10010004, 0); // Class 1
    InitializeEvent(1, 10010004, 0); // Class 2
    InitializeEvent(2, 10010004, 0); // Class 3
});

// Set Random Class
$Event(10010004, Default, function() {
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

// Class Preview
$Event(10010005, Restart, function(X0_4, X4_4, X8_4) {
    WaitFor(ActionButtonInArea(X0_4, X4_4));
    DisplayFullScreenMessage(X8_4);
    
    RestartEvent();
});

// Apply Rebirth Class Change
$Event(10010010, Restart, function() {
    SetEventFlag(0, 1047610021, OFF); // Reset on reloads
    
    WaitFor(EventFlag(1047610021));
    
    // Wretch
    if(EventFlag(1047610200))
    {
        // Accursed
        if(EventFlag(1047610100))
        {
            ChangeCharacter(3010);
        }
        else
        {
            ChangeCharacter(3000);
        }
    }
    
    // Soldier
    if(EventFlag(1047610201))
    {
        // Knight
        if(EventFlag(1047610101))
        {
            ChangeCharacter(3011);
        }
        else
        {
            ChangeCharacter(3001);   
        }
    }
    
    // Barbarian
    if(EventFlag(1047610202))
    {
        // Warlord
        if(EventFlag(1047610102))
        {
            ChangeCharacter(3012);
        }
        else
        {
            ChangeCharacter(3002);   
        }
    }
    
    // Knave
    if(EventFlag(1047610203))
    {
        // Assassin
        if(EventFlag(1047610103))
        {
            ChangeCharacter(3013);
        }
        else
        {   
            ChangeCharacter(3003);
        }
    }
    
    // Exile
    if(EventFlag(1047610204))
    {
        // Mercenary
        if(EventFlag(1047610104))
        {
            ChangeCharacter(3014);
        }
        else
        {  
            ChangeCharacter(3004);
        }
    }
    
    // Samurai
    if(EventFlag(1047610205))
    {
        // Shinobi
        if(EventFlag(1047610105))
        {
            ChangeCharacter(3015);
        }
        else
        {   
            ChangeCharacter(3005);
        }
    }
    
    // Archer
    if(EventFlag(1047610206))
    {
        // Ranger
        if(EventFlag(1047610106))
        {
            ChangeCharacter(3016);
        }
        else
        {
            ChangeCharacter(3006);
        }
    }
    
    // Apprentice
    if(EventFlag(1047610207))
    {
        // Sorcerer
        if(EventFlag(1047610107))
        {
            ChangeCharacter(3017);
        }
        else
        {
            ChangeCharacter(3007);
        }
    }
    
    // Disciple
    if(EventFlag(1047610208))
    {
        // Priest
        if(EventFlag(1047610108))
        {
            ChangeCharacter(3018);
        }
        else
        {   
            ChangeCharacter(3008);
        }
    }
    
    // Apostle
    if(EventFlag(1047610209))
    {
        // Noble
        if(EventFlag(1047610109))
        {
            ChangeCharacter(3019);
        }
        else
        {
            ChangeCharacter(3009);
        }
    }
    
    // Clear the status bars on class change
    SetSpEffect(10000, 10001040);
    SetSpEffect(10000, 10001041);
    SetSpEffect(10000, 10001042);
    SetSpEffect(10000, 10001043);
    SetSpEffect(10000, 10001044);
    SetSpEffect(10000, 10001045);
    SetSpEffect(10000, 10001046);
    
    WaitFixedTimeSeconds(0.05);
    
    // Clear the status bars on class change
    SetSpEffect(10000, 10001040);
    SetSpEffect(10000, 10001041);
    SetSpEffect(10000, 10001042);
    SetSpEffect(10000, 10001043);
    SetSpEffect(10000, 10001044);
    SetSpEffect(10000, 10001045);
    SetSpEffect(10000, 10001046);
});

// Blacksmith
$Event(10010020, Restart, function() {
    DisableNetworkSync();
    WaitFixedTimeFrames(1);
    
    DisableCharacter(10010870);
    SetCharacterBackreadState(10010870, true);
    SetCharacterTalkRange(10010870, 50);

    SetCharacterBackreadState(10010870, false);
    EnableCharacter(10010870);
    ForceAnimationPlayback(10010870, 930010, false, false, false);
});

// Enchantress
$Event(10010030, Restart, function() {
    DisableNetworkSync();
    WaitFixedTimeFrames(1);
    
    DisableCharacter(10010875);
    SetCharacterBackreadState(10010875, true);
    SetCharacterTalkRange(10010875, 50);

    SetCharacterBackreadState(10010875, false);
    EnableCharacter(10010875);
    //ForceAnimationPlayback(10010870, 930010, false, false, false);
});

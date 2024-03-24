// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common_func.emevd N:\GR\data\Param\event\common_macro.emevd      
// @linked    [0,82]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    InitializeEvent(0, 45020010, 0);
    InitializeEvent(0, 45020020, 0);
    InitializeEvent(0, 45020030, 0);
});

// Apply Rebirth Class Change
$Event(45020010, Restart, function() {
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
    
    WaitFixedTimeSeconds(0.25);
    
    // Clear the status bars on class change
    SetSpEffect(10000, 10001040);
    SetSpEffect(10000, 10001041);
    SetSpEffect(10000, 10001042);
    SetSpEffect(10000, 10001043);
    SetSpEffect(10000, 10001044);
    SetSpEffect(10000, 10001045);
    SetSpEffect(10000, 10001046);
});

// Enter Deathtrap Dungeon
$Event(45020020, Restart, function() {
    DisableNetworkSync();
    
    WaitFor(ActionButtonInArea(7000, 45020400));
    
    SetEventFlag(0, 1047610021, ON);
    
    WaitFixedTimeSeconds(0.5);
    
    InitializeCommonEvent(0, 98006000, 0); // Level Warp
});

// Setup
$Event(45020030, Restart, function() {
    SetCurrentTime(0, 0, 0, false, false, false, 0, 0, 0);
    SetPlayerRespawnPoint(10012020);
});


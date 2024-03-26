// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common_func.emevd N:\GR\data\Param\event\common_macro.emevd      
// @linked    [0,82]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    InitializeEvent(0, 45020020, 0);
    InitializeEvent(0, 45020030, 0);
});


// Enter Deathtrap Dungeon
$Event(45020020, Restart, function() {
    DisableNetworkSync();
    
    WaitFor(ActionButtonInArea(7000, 45020400));
    
    WaitFixedTimeSeconds(0.25);
    
    InitializeCommonEvent(0, 98006000, 0); // Level Warp
});

// Setup
$Event(45020030, Restart, function() {
    SetCurrentTime(0, 0, 0, false, false, false, 0, 0, 0);
    SetPlayerRespawnPoint(10012020);
});

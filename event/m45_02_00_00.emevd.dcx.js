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

// Set Respawn
$Event(45020010, Restart, function() {
    SetPlayerRespawnPoint(45020300);
    SaveRequest();
});

// Enter Deathtrap Dungeon
$Event(45020020, Restart, function() {
    DisableNetworkSync();
    
    WaitFor(ActionButtonInArea(7000, 45020400));
    
    // Jail spawn
    SetPlayerRespawnPoint(45020301);
    
    InitializeCommonEvent(0, 98006000, 0); // Level Warp
    
    WaitFixedTimeSeconds(1);
    RestartEvent();
});

// Time
$Event(45020030, Restart, function() {
    SetCurrentTime(0, 0, 0, false, false, false, 0, 0, 0);
    //ChangeWeather(Weather.RainyHeavyFog, 300, true);
});

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
    InitializeEvent(0, 10010030, 0);
    InitializeEvent(0, 10010040, 0);
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
    //EndIf(EventFlag(1047610005));
    WaitFor(InArea(10000, 10012510, 1));
    FadeToBlack(1.0, 2.0, false, 0);
    SetEventFlag(0, 1047610005, ON);
    WaitFixedTimeSeconds(1.0);
    SetEventFlag(0, 1047610010, ON);
});

// Reset Class after dying
$Event(10010030, Restart, function() {
    EndIf(!EventFlag(1047610005)); // Ignore first spawn
    ChangeCharacter(3009);
});

// Apply Rebirth Class/Trait/etc
$Event(10010040, Restart, function() {
    // 10010850
});

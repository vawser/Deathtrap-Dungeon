# -*- coding: utf-8 -*-
def t000001000_1():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    t000001000_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000,
                  z5=1000000, mode1=1, mode2=1)
    Quit()

def t000001000_1000():
    """State 0,2,3"""
    assert t000001000_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t000001000_2000():
    """State 0,2,3"""
    assert t000001000_x36()
    """State 1"""
    c1_120(2000)
    Quit()

def t000001000_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                  flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1 or
                GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not
              GetEventFlag(flag11) and not GetEventFlag(flag12)):
            pass
        # actionbutton:6210:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t000001000_x1():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t000001000_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001000_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t000001000_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t000001000_x1()
    else:
        """State 4,7"""
        call = t000001000_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t000001000_x1()
    """State 9"""
    return 0

def t000001000_x4():
    """State 0,1"""
    assert t000001000_x1()
    """State 2"""
    return 0

def t000001000_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000,
                  z5=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t000001000_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z2=z2, z3=z3, z4=z4, z5=z5, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t000001000_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t000001000_x6(val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000, z5=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t000001000_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z3=z3, z4=z4, z5=z5)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t000001000_x13(val1=val1, z2=z2)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode1 == 1), -1, 0)
                c5_139(1 == (mode2 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag8) == 1:
            Goto('L0')
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t000001000_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t000001000_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t000001000_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t000001000_x7(val2=10, val3=12):
    """State 0,1"""
    call = t000001000_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t000001000_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t000001000_x8(flag1=3223, val2=10, val3=12):
    """State 0,8"""
    assert t000001000_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t000001000_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001000_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t000001000_x9(actionbutton1=6210, flag4=6000, flag5=6001, z3=1000000, z4=1000000, z5=1000000):
    """State 0,1"""
    call = t000001000_x10(z11=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t000001000_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001000_x10(z11=_, val6=_):
    """State 0,1"""
    if f203(z11) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z11)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t000001000_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t000001000_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t000001000_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001000_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t000001000_x12():
    """State 0,1"""
    assert t000001000_x10(z11=1101, val6=1101)
    """State 2"""
    return 0

def t000001000_x13(val1=5, z2=1):
    """State 0,2"""
    assert t000001000_x23()
    """State 1"""
    call = t000001000_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t000001000_x25()
    """State 4"""
    return 0

def t000001000_x14():
    """State 0,1"""
    assert t000001000_x10(z11=1000, val6=1000)
    """State 2"""
    return 0

def t000001000_x15(val5=30):
    """State 0,1"""
    call = t000001000_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t000001000_x26()
    """State 3"""
    return 0

def t000001000_x16():
    """State 0,1"""
    assert t000001000_x10(z11=1100, val6=1100)
    """State 2"""
    return 0

def t000001000_x17(val2=10, val3=12):
    """State 0,5"""
    assert t000001000_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t000001000_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t000001000_x28()
    """Unused"""
    """State 6"""
    return 0

def t000001000_x18():
    """State 0,2"""
    call = t000001000_x10(z11=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t000001000_x19():
    """State 0,1"""
    assert t000001000_x10(z11=1001, val6=1001)
    """State 2"""
    return 0

def t000001000_x20():
    """State 0,1"""
    assert t000001000_x10(z11=1103, val6=1103)
    """State 2"""
    return 0

def t000001000_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t000001000_x22(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z2=1, z3=1000000, z4=1000000,
                   z5=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t000001000_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z2=z2,
                             z3=z3, z4=z4, z5=z5, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t000001000_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t000001000_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t000001000_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t000001000_x23():
    """State 0,1"""
    assert t000001000_x24()
    """State 2"""
    return 0

def t000001000_x24():
    """State 0,1"""
    assert t000001000_x10(z11=1104, val6=1104)
    """State 2"""
    return 0

def t000001000_x25():
    """State 0,1"""
    call = t000001000_x10(z11=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t000001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001000_x26():
    """State 0,1"""
    call = t000001000_x10(z11=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t000001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001000_x27():
    """State 0,1"""
    call = t000001000_x10(z11=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t000001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001000_x28():
    """State 0,1"""
    call = t000001000_x10(z11=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t000001000_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001000_x29(z9=_, z10=_):
    """State 0,4"""
    assert t000001000_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(z9, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not z10:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t000001000_x30(z6=_, z7=_, z8=_):
    """State 0,5"""
    assert t000001000_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z7, 1)
    """State 1"""
    TalkToPlayer(z6, -1, -1, 1)
    """State 4"""
    if not z8:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t000001000_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001000_x32():
    """State 0,1"""
    assert t000001000_x10(z11=1002, val6=1002)
    """State 2"""
    return 0

def t000001000_x33():
    """State 0,1"""
    assert t000001000_x1()
    """State 2"""
    return 0

def t000001000_x34():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0

def t000001000_x35():
    """State 0"""
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 8"""
    assert t000001000_x100()
    """State 9"""
    return 0

def t000001000_x36():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    assert (t000001000_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=6000))
    """State 4"""
    return 0

def t000001000_x100():
    while True:
        """State 0"""
        ClearTalkListData()
        c1_110()
        
        # Purchase
        # AddTalkListData(1, 80106001, -1)
        
        # Attune Block
        AddTalkListData(2, 80106000, -1)
        
        # Toggle Shinobi Sight on
        AddTalkListDataIf(not GetEventFlag(1047610630), 3, 80106700, -1)
        
        # Toggle Shinobi Sight off
        AddTalkListDataIf(GetEventFlag(1047610630) == 1, 4, 80106701, -1)
        
        # Turn in the Tome of Holy Burst
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 3800, 4, 1, 0), 10, 80106500, -1)
        
        # Turn in the Tome of Moonlit Burst
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 3801, 4, 1, 0), 11, 80106501, -1)
        
        # Turn in the Tome of Searing Burst
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 3802, 4, 1, 0), 12, 80106502, -1)
        
        # Turn in the Tome of Vampiric Burst
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 3803, 4, 1, 0), 13, 80106503, -1)
        
        # Turn in Me, You and Block
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 3810, 4, 1, 0), 20, 80106504, -1)
        
        # Turn in Rock 'n' Block
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 3820, 4, 1, 0), 21, 80106505, -1)
        
        # Leave
        AddTalkListData(99, 20000009, -1)
        
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        """State 1"""
        if GetTalkListEntryResult() == 1:
            """State 2"""
            OpenRegularShop(8010000, 8010999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Attune Block
        elif GetTalkListEntryResult() == 2:
            """State 3"""
            assert t000001000_x101()
        # Toggle Shinobi Sight on
        elif GetTalkListEntryResult() == 3:
            """State 4"""
            assert t000001000_x110(action1=80106710)
            """State 5"""
            SetEventFlag(1047610630, 1)
            return 0
        # Toggle Shinobi Sight off
        elif GetTalkListEntryResult() == 4:
            """State 7"""
            assert t000001000_x110(action1=80106711)
            """State 9"""
            SetEventFlag(1047610630, 0)
            return 0
        # Turn in the Tome of Holy Burst
        elif GetTalkListEntryResult() == 10:
            """State 10"""
            assert t000001000_x110(action1=80106600)
            """State 11"""
            SetEventFlag(1047610621, 1)
            PlayerEquipmentQuantityChange(3, 3800, -99)
        # Turn in the Tome of Moonlit Burst
        elif GetTalkListEntryResult() == 11:
            """State 12"""
            assert t000001000_x110(action1=80106601)
            """State 13"""
            SetEventFlag(1047610622, 1)
            PlayerEquipmentQuantityChange(3, 3801, -99)
        # Turn in the Tome of Searing Burst
        elif GetTalkListEntryResult() == 12:
            """State 14"""
            assert t000001000_x110(action1=80106602)
            """State 15"""
            SetEventFlag(1047610623, 1)
            PlayerEquipmentQuantityChange(3, 3802, -99)
        # Turn in the Tome of Vampiric Burst
        elif GetTalkListEntryResult() == 13:
            """State 16"""
            assert t000001000_x110(action1=80106603)
            """State 17"""
            SetEventFlag(1047610624, 1)
            PlayerEquipmentQuantityChange(3, 3803, -99)
        # Turn in Me, You and Block
        elif GetTalkListEntryResult() == 20:
            """State 18"""
            assert t000001000_x110(action1=80106400)
            """State 19"""
            SetEventFlag(1047610611, 1)
            PlayerEquipmentQuantityChange(3, 3810, -99)
        # Turn in Rock 'n' Block
        elif GetTalkListEntryResult() == 21:
            """State 20"""
            assert t000001000_x110(action1=80106401)
            """State 21"""
            SetEventFlag(1047610612, 1)
            PlayerEquipmentQuantityChange(3, 3820, -99)
        else:
            """State 6,8"""
            return 0

def t000001000_x101():
    """State 0"""
    ClearTalkListData()
    c1_110()
    
    # Block Type: Storm
    AddTalkListDataIf(GetEventFlag(1047610620) == 1 and not GetEventFlag(1047610600), 1, 80106100, -1)
    
    # Block Type: Storm (selected)
    AddTalkListDataIf(GetEventFlag(1047610620) == 1 and GetEventFlag(1047610600) == 1, 10, 80106200, -1)
    
    # Block Type: Holy
    AddTalkListDataIf(GetEventFlag(1047610621) == 1 and not GetEventFlag(1047610601), 2, 80106101, -1)
    
    # Block Type: Holy (selected)
    AddTalkListDataIf(GetEventFlag(1047610621) == 1 and GetEventFlag(1047610601) == 1, 11, 80106201, -1)
    
    # Block Type: Moon
    AddTalkListDataIf(GetEventFlag(1047610622) == 1 and not GetEventFlag(1047610602), 3, 80106102, -1)
    
    # Block Type: Moon (selected)
    AddTalkListDataIf(GetEventFlag(1047610622) == 1 and GetEventFlag(1047610602) == 1, 12, 80106202, -1)
    
    # Block Type: Fire
    AddTalkListDataIf(GetEventFlag(1047610623) == 1 and not GetEventFlag(1047610603), 4, 80106103, -1)
    
    # Block Type: Fire (selected)
    AddTalkListDataIf(GetEventFlag(1047610623) == 1 and GetEventFlag(1047610603) == 1, 13, 80106203, -1)
    
    # Block Type: Thorn
    AddTalkListDataIf(GetEventFlag(1047610624) == 1 and not GetEventFlag(1047610604), 5, 80106104, -1)
    
    # Block Type: Thorn (selected)
    AddTalkListDataIf(GetEventFlag(1047610624) == 1 and GetEventFlag(1047610604) == 1, 14, 80106204, -1)
    
    # Leave
    AddTalkListData(99, 20000009, -1)
    
    ShowShopMessage(1)
    assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    
    """State 1"""
    # Block Type: Storm
    if GetTalkListEntryResult() == 1:
        """State 2"""
        assert t000001000_x110(action1=80106300)
        """State 3"""
        assert t000001000_x111(z1=1047610600)
        """State 4"""
        return 0
    # Block Type: Holy
    elif GetTalkListEntryResult() == 2:
        """State 5"""
        assert t000001000_x110(action1=80106301)
        """State 7"""
        assert t000001000_x111(z1=1047610601)
        """State 9"""
        return 0
    # Block Type: Moon
    elif GetTalkListEntryResult() == 3:
        """State 10"""
        assert t000001000_x110(action1=80106302)
        """State 11"""
        assert t000001000_x111(z1=1047610602)
        """State 12"""
        return 0
    # Block Type: Fire
    elif GetTalkListEntryResult() == 4:
        """State 13"""
        assert t000001000_x110(action1=80106303)
        """State 14"""
        assert t000001000_x111(z1=1047610603)
        """State 15"""
        return 0
    # Block Type: Thorn
    elif GetTalkListEntryResult() == 5:
        """State 16"""
        assert t000001000_x110(action1=80106304)
        """State 17"""
        assert t000001000_x111(z1=1047610604)
        """State 18"""
        return 0
    elif GetTalkListEntryResult() >= 10:
        """State 19"""
        return 0
    else:
        """State 6,8"""
        return 0

def t000001000_x110(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t000001000_x111(z1=_):
    """State 0"""
    SetEventFlag(1047610600, 0)
    SetEventFlag(1047610601, 0)
    SetEventFlag(1047610602, 0)
    SetEventFlag(1047610603, 0)
    SetEventFlag(1047610604, 0)
    SetEventFlag(z1, 1)
    return 0


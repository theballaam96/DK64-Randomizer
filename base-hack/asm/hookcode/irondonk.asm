permaLossTagCheck:
    jal determineKongUnlock
    lw $a0, 0x58 ($t5)
    j 0x80682F48
    nop

permaLossTagSet:
    jal unlockKongPermaLoss
    lw $a0, 0x58 ($t9)
    j 0x80683640
    nop

permaLossTagDisplayCheck:
    jal determineKongUnlock
    or $a1, $s0, $zero
    j 0x806840e0
    nop

alterWaterSurface:
    sb $zero, 0x4A ($v0)
    lbu $v1, 0x66 ($s2)
    beqz $v1, alterWaterSurface_isWater
    addiu $at, $zero, 0x3
    bne $v1, $at, alterWaterSurface_finish
    nop

    alterWaterSurface_isWater:
        addiu $at, $zero, 0x1
        sb $at, 0x4A ($v0)
        addiu $at, $zero, 0x7
        sb $at, 0x66 ($s2)

    alterWaterSurface_finish:
        j 0x8065f298
        sb $zero, 0x4B ($v0)
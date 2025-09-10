import FWCore.ParameterSet.Config as cms

def HBHEPhase1Reconstructor(*args, **kwargs):
  mod = cms.EDProducer('HBHEPhase1Reconstructor',
    digiLabelQIE8 = cms.InputTag('hcalDigis'),
    processQIE8 = cms.bool(True),
    digiLabelQIE11 = cms.InputTag('hcalDigis'),
    processQIE11 = cms.bool(True),
    tsFromDB = cms.bool(False),
    recoParamsFromDB = cms.bool(True),
    saveEffectivePedestal = cms.bool(False),
    dropZSmarkedPassed = cms.bool(True),
    makeRecHits = cms.bool(True),
    saveInfos = cms.bool(False),
    saveDroppedInfos = cms.bool(False),
    use8ts = cms.bool(True),
    sipmQTSShift = cms.int32(0),
    sipmQNTStoSum = cms.int32(3),
    algorithm = cms.PSet(
      applyTimeSlewM3 = cms.bool(True),
      timeSlewParsType = cms.int32(3),
      respCorrM3 = cms.double(1),
      applyPedConstraint = cms.bool(True),
      applyTimeConstraint = cms.bool(True),
      applyPulseJitter = cms.bool(False),
      applyTimeSlew = cms.bool(True),
      ts4Min = cms.double(0),
      ts4Max = cms.vdouble(
        100,
        20000,
        30000
      ),
      pulseJitter = cms.double(1),
      meanPed = cms.double(0),
      meanTime = cms.double(0),
      timeSigmaHPD = cms.double(5),
      timeSigmaSiPM = cms.double(2.5),
      timeMin = cms.double(-12.5),
      timeMax = cms.double(12.5),
      ts4chi2 = cms.vdouble(
        15,
        15
      ),
      fitTimes = cms.int32(1),
      firstSampleShift = cms.int32(0),
      samplesToAdd = cms.int32(2),
      correctForPhaseContainment = cms.bool(True),
      correctionPhaseNS = cms.double(6),
      applyFixPCC = cms.bool(False),
      calculateArrivalTime = cms.bool(True),
      timeAlgo = cms.int32(2),
      thEnergeticPulses = cms.double(5),
      dynamicPed = cms.bool(False),
      ts4Thresh = cms.double(0),
      chiSqSwitch = cms.double(15),
      activeBXs = cms.vint32(
        -3,
        -2,
        -1,
        0,
        1,
        2,
        3,
        4
      ),
      nMaxItersMin = cms.int32(500),
      nMaxItersNNLS = cms.int32(500),
      deltaChiSqThresh = cms.double(0.001),
      nnlsThresh = cms.double(1e-11),
      Class = cms.string('SimpleHBHEPhase1Algo'),
      tdcTimeShift = cms.double(0),
      useM2 = cms.bool(False),
      useM3 = cms.bool(True),
      useMahi = cms.bool(True),
      applyLegacyHBMCorrection = cms.bool(True)
    ),
    algoConfigClass = cms.string(''),
    setNegativeFlagsQIE8 = cms.bool(True),
    setNegativeFlagsQIE11 = cms.bool(False),
    setNoiseFlagsQIE8 = cms.bool(True),
    setNoiseFlagsQIE11 = cms.bool(False),
    setPulseShapeFlagsQIE8 = cms.bool(True),
    setPulseShapeFlagsQIE11 = cms.bool(False),
    setLegacyFlagsQIE8 = cms.bool(True),
    setLegacyFlagsQIE11 = cms.bool(False),
    flagParametersQIE8 = cms.PSet(
      nominalPedestal = cms.double(3),
      hitEnergyMinimum = cms.double(1),
      hitMultiplicityThreshold = cms.int32(17),
      pulseShapeParameterSets = cms.VPSet(
        cms.PSet(
          pulseShapeParameters = cms.vdouble(
            0,
            100,
            -50,
            0,
            -15,
            0.15
          )
        ),
        cms.PSet(
          pulseShapeParameters = cms.vdouble(
            100,
            2000,
            -50,
            0,
            -5,
            0.05
          )
        ),
        cms.PSet(
          pulseShapeParameters = cms.vdouble(
            2000,
            1000000,
            -50,
            0,
            95,
            0
          )
        ),
        cms.PSet(
          pulseShapeParameters = cms.vdouble(
            -1000000,
            1000000,
            45,
            0.1,
            1000000,
            0
          )
        ),
        template = cms.PSetTemplate(
          pulseShapeParameters = cms.vdouble(
            0,
            100,
            -50,
            0,
            -15,
            0.15
          )
        )
      )
    ),
    flagParametersQIE11 = cms.PSet(),
    pulseShapeParametersQIE8 = cms.PSet(
      MinimumChargeThreshold = cms.double(20),
      TS4TS5ChargeThreshold = cms.double(70),
      TS3TS4ChargeThreshold = cms.double(70),
      TS3TS4UpperChargeThreshold = cms.double(20),
      TS5TS6ChargeThreshold = cms.double(70),
      TS5TS6UpperChargeThreshold = cms.double(20),
      R45PlusOneRange = cms.double(0.2),
      R45MinusOneRange = cms.double(0.2),
      TrianglePeakTS = cms.uint32(10000),
      LinearThreshold = cms.vdouble(
        20,
        100,
        100000
      ),
      LinearCut = cms.vdouble(
        -3,
        -0.054,
        -0.054
      ),
      RMS8MaxThreshold = cms.vdouble(
        20,
        100,
        100000
      ),
      RMS8MaxCut = cms.vdouble(
        -13.5,
        -11.5,
        -11.5
      ),
      LeftSlopeThreshold = cms.vdouble(
        250,
        500,
        100000
      ),
      LeftSlopeCut = cms.vdouble(
        5,
        2.55,
        2.55
      ),
      RightSlopeThreshold = cms.vdouble(
        250,
        400,
        100000
      ),
      RightSlopeCut = cms.vdouble(
        5,
        4.15,
        4.15
      ),
      RightSlopeSmallThreshold = cms.vdouble(
        150,
        200,
        100000
      ),
      RightSlopeSmallCut = cms.vdouble(
        1.08,
        1.16,
        1.16
      ),
      MinimumTS4TS5Threshold = cms.double(100),
      TS4TS5UpperThreshold = cms.vdouble(
        70,
        90,
        100,
        400
      ),
      TS4TS5UpperCut = cms.vdouble(
        1,
        0.8,
        0.75,
        0.72
      ),
      TS4TS5LowerThreshold = cms.vdouble(
        100,
        120,
        160,
        200,
        300,
        500
      ),
      TS4TS5LowerCut = cms.vdouble(
        -1,
        -0.7,
        -0.5,
        -0.4,
        -0.3,
        0.1
      ),
      UseDualFit = cms.bool(True),
      TriangleIgnoreSlow = cms.bool(False)
    ),
    pulseShapeParametersQIE11 = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

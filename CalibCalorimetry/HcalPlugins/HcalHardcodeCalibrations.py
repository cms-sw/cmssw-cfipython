import FWCore.ParameterSet.Config as cms

def HcalHardcodeCalibrations(*args, **kwargs):
  mod = cms.ESSource('HcalHardcodeCalibrations',
    iLumi = cms.double(-1),
    HBRecalibration = cms.bool(False),
    HBreCalibCutoff = cms.double(20),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HFRecalibration = cms.bool(False),
    GainWidthsForTrigPrims = cms.bool(False),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    testHFQIE10 = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    killHE = cms.bool(False),
    useLayer0Weight = cms.bool(False),
    useIeta18depth1 = cms.bool(True),
    toGet = cms.untracked.vstring(),
    fromDDD = cms.untracked.bool(False),
    hb = cms.PSet(
      gain = cms.vdouble(0.19),
      gainWidth = cms.vdouble(0),
      pedestal = cms.double(3),
      pedestalWidth = cms.double(0.55),
      zsThreshold = cms.int32(8),
      qieOffset = cms.vdouble(
        -0.49,
        1.8,
        7.2,
        37.9
      ),
      qieSlope = cms.vdouble(
        0.912,
        0.917,
        0.922,
        0.923
      ),
      qieType = cms.int32(0),
      mcShape = cms.int32(125),
      recoShape = cms.int32(105),
      photoelectronsToAnalog = cms.double(0),
      darkCurrent = cms.vdouble(0),
      noiseCorrelation = cms.vdouble(0),
      doRadiationDamage = cms.bool(False),
      noiseThreshold = cms.double(0),
      seedThreshold = cms.double(0.1)
    ),
    hbUpgrade = cms.PSet(
      gain = cms.vdouble(0.00111111111111),
      gainWidth = cms.vdouble(0),
      pedestal = cms.double(18),
      pedestalWidth = cms.double(5),
      zsThreshold = cms.int32(3),
      qieOffset = cms.vdouble(
        0,
        0,
        0,
        0
      ),
      qieSlope = cms.vdouble(
        0.333,
        0.333,
        0.333,
        0.333
      ),
      qieType = cms.int32(2),
      mcShape = cms.int32(206),
      recoShape = cms.int32(206),
      photoelectronsToAnalog = cms.double(57.5),
      darkCurrent = cms.vdouble(0.055),
      noiseCorrelation = cms.vdouble(0.26),
      doRadiationDamage = cms.bool(True),
      radiationDamage = cms.PSet(
        temperatureBase = cms.double(20),
        temperatureNew = cms.double(-5),
        intlumiOffset = cms.double(150),
        depVsTemp = cms.double(0.0631),
        intlumiToNeutrons = cms.double(367000000),
        depVsNeutrons = cms.vdouble(
          5.69e-11,
          7.9e-11
        )
      ),
      noiseThreshold = cms.double(0),
      seedThreshold = cms.double(0.1)
    ),
    he = cms.PSet(
      gain = cms.vdouble(0.23),
      gainWidth = cms.vdouble(0),
      pedestal = cms.double(3),
      pedestalWidth = cms.double(0.79),
      zsThreshold = cms.int32(9),
      qieOffset = cms.vdouble(
        -0.38,
        2,
        7.6,
        39.6
      ),
      qieSlope = cms.vdouble(
        0.912,
        0.916,
        0.92,
        0.922
      ),
      qieType = cms.int32(0),
      mcShape = cms.int32(125),
      recoShape = cms.int32(105),
      photoelectronsToAnalog = cms.double(0),
      darkCurrent = cms.vdouble(0),
      noiseCorrelation = cms.vdouble(0),
      doRadiationDamage = cms.bool(False),
      noiseThreshold = cms.double(0),
      seedThreshold = cms.double(0.1)
    ),
    heUpgrade = cms.PSet(
      gain = cms.vdouble(0.00111111111111),
      gainWidth = cms.vdouble(0),
      pedestal = cms.double(18),
      pedestalWidth = cms.double(5),
      zsThreshold = cms.int32(3),
      qieOffset = cms.vdouble(
        0,
        0,
        0,
        0
      ),
      qieSlope = cms.vdouble(
        0.333,
        0.333,
        0.333,
        0.333
      ),
      qieType = cms.int32(2),
      mcShape = cms.int32(206),
      recoShape = cms.int32(206),
      photoelectronsToAnalog = cms.double(57.5),
      darkCurrent = cms.vdouble(0.055),
      noiseCorrelation = cms.vdouble(0.26),
      doRadiationDamage = cms.bool(True),
      radiationDamage = cms.PSet(
        temperatureBase = cms.double(20),
        temperatureNew = cms.double(5),
        intlumiOffset = cms.double(75),
        depVsTemp = cms.double(0.0631),
        intlumiToNeutrons = cms.double(292000000),
        depVsNeutrons = cms.vdouble(
          5.69e-11,
          7.9e-11
        )
      ),
      noiseThreshold = cms.double(0),
      seedThreshold = cms.double(0.1)
    ),
    hf = cms.PSet(
      gain = cms.vdouble(
        0.14,
        0.135
      ),
      gainWidth = cms.vdouble(
        0,
        0
      ),
      pedestal = cms.double(3),
      pedestalWidth = cms.double(0.84),
      zsThreshold = cms.int32(-9999),
      qieOffset = cms.vdouble(
        -0.87,
        1.4,
        7.8,
        -29.6
      ),
      qieSlope = cms.vdouble(
        0.359,
        0.358,
        0.36,
        0.367
      ),
      qieType = cms.int32(0),
      mcShape = cms.int32(301),
      recoShape = cms.int32(301),
      photoelectronsToAnalog = cms.double(0),
      darkCurrent = cms.vdouble(0),
      noiseCorrelation = cms.vdouble(0),
      doRadiationDamage = cms.bool(False),
      noiseThreshold = cms.double(0),
      seedThreshold = cms.double(0.1)
    ),
    hfUpgrade = cms.PSet(
      gain = cms.vdouble(
        0.14,
        0.135
      ),
      gainWidth = cms.vdouble(
        0,
        0
      ),
      pedestal = cms.double(13.33),
      pedestalWidth = cms.double(3.33),
      zsThreshold = cms.int32(-9999),
      qieOffset = cms.vdouble(
        0.0697,
        -0.7405,
        12.38,
        -671.9
      ),
      qieSlope = cms.vdouble(
        0.297,
        0.298,
        0.298,
        0.313
      ),
      qieType = cms.int32(1),
      mcShape = cms.int32(301),
      recoShape = cms.int32(301),
      photoelectronsToAnalog = cms.double(0),
      darkCurrent = cms.vdouble(0),
      noiseCorrelation = cms.vdouble(0),
      doRadiationDamage = cms.bool(False),
      noiseThreshold = cms.double(0),
      seedThreshold = cms.double(0.1)
    ),
    HFRecalParameterBlock = cms.PSet(
      HFdepthOneParameterA = cms.vdouble(),
      HFdepthOneParameterB = cms.vdouble(),
      HFdepthTwoParameterA = cms.vdouble(),
      HFdepthTwoParameterB = cms.vdouble()
    ),
    ho = cms.PSet(
      gain = cms.vdouble(
        0.006,
        0.0087
      ),
      gainWidth = cms.vdouble(
        0,
        0
      ),
      pedestal = cms.double(11),
      pedestalWidth = cms.double(0.57),
      zsThreshold = cms.int32(24),
      qieOffset = cms.vdouble(
        -0.44,
        1.4,
        7.1,
        38.5
      ),
      qieSlope = cms.vdouble(
        0.907,
        0.915,
        0.92,
        0.921
      ),
      qieType = cms.int32(0),
      mcShape = cms.int32(201),
      recoShape = cms.int32(201),
      photoelectronsToAnalog = cms.double(4),
      darkCurrent = cms.vdouble(0),
      noiseCorrelation = cms.vdouble(0),
      doRadiationDamage = cms.bool(False),
      noiseThreshold = cms.double(0),
      seedThreshold = cms.double(0.1)
    ),
    SiPMCharacteristics = cms.VPSet(
      cms.PSet()
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

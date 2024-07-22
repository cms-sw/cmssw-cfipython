import FWCore.ParameterSet.Config as cms

def GEMDigiProducer(**kwargs):
  mod = cms.EDProducer('GEMDigiProducer',
    inputCollection = cms.string('g4SimHitsMuonGEMHits'),
    mixLabel = cms.string('mix'),
    signalPropagationSpeed = cms.double(0.66),
    timeResolution = cms.double(18),
    timeJitter = cms.double(1),
    averageShapingTime = cms.double(50),
    averageEfficiency = cms.double(0.98),
    averageNoiseRate = cms.double(0.001),
    minBunch = cms.int32(-5),
    maxBunch = cms.int32(3),
    fixedRollRadius = cms.bool(True),
    digitizeOnlyMuons = cms.bool(False),
    simulateBkgNoise = cms.bool(False),
    simulateNoiseCLS = cms.bool(True),
    simulateElectronBkg = cms.bool(True),
    simulateIntrinsicNoise = cms.bool(False),
    instLumi = cms.double(7.5),
    rateFact = cms.double(1),
    bxWidth = cms.double(2.5e-08),
    referenceInstLumi = cms.double(5),
    resolutionX = cms.double(0.03),
    GE11ModNeuBkgParam0 = cms.double(5710.23),
    GE11ModNeuBkgParam1 = cms.double(-43.3928),
    GE11ModNeuBkgParam2 = cms.double(0.0863681),
    GE21ModNeuBkgParam0 = cms.double(1440.44),
    GE21ModNeuBkgParam1 = cms.double(-7.48607),
    GE21ModNeuBkgParam2 = cms.double(0.0103078),
    GE11ElecBkgParam0 = cms.double(406.249),
    GE11ElecBkgParam1 = cms.double(-2.90939),
    GE11ElecBkgParam2 = cms.double(0.00548191),
    GE21ElecBkgParam0 = cms.double(97.0505),
    GE21ElecBkgParam1 = cms.double(-43.3928),
    GE21ElecBkgParam2 = cms.double(0.000550599),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
import FWCore.ParameterSet.Config as cms

def CTPPSPixelDigiProducer(*args, **kwargs):
  mod = cms.EDProducer('CTPPSPixelDigiProducer',
    ROUList = cms.vstring('CTPPSPixelHits'),
    RPixVerbosity = cms.int32(0),
    CTPPSPixelDigiSimHitRelationsPersistence = cms.bool(False),
    RPixEquivalentNoiseCharge = cms.double(1000),
    RPixNoNoise = cms.bool(False),
    RPixGeVPerElectron = cms.double(3.61e-09),
    RPixInterSmearing = cms.vdouble(0.011),
    RPixLandauFluctuations = cms.bool(True),
    RPixChargeDivisions = cms.int32(20),
    RPixDeltaProductionCut = cms.double(0.120425),
    ChargeMapFile2E = cms.string('SimPPS/PPSPixelDigiProducer/data/PixelChargeMap.txt'),
    ChargeMapFile2E_2X = cms.string('SimPPS/PPSPixelDigiProducer/data/PixelChargeMap_2X.txt'),
    ChargeMapFile2E_2Y = cms.string('SimPPS/PPSPixelDigiProducer/data/PixelChargeMap_2Y.txt'),
    ChargeMapFile2E_2X2Y = cms.string('SimPPS/PPSPixelDigiProducer/data/PixelChargeMap_2X2Y.txt'),
    RPixCoupling = cms.double(0.25),
    RPixDummyROCThreshold = cms.double(1900),
    RPixDummyROCElectronPerADC = cms.double(135),
    VCaltoElectronGain = cms.int32(50),
    VCaltoElectronOffset = cms.int32(-411),
    doSingleCalibration = cms.bool(False),
    RPixDeadPixelProbability = cms.double(0.001),
    RPixDeadPixelSimulationOn = cms.bool(True),
    mixLabel = cms.string('mix'),
    InputCollection = cms.string('g4SimHitsCTPPSPixelHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

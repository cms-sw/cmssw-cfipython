import FWCore.ParameterSet.Config as cms

def CTPPSPixelClusterProducer(**kwargs):
  mod = cms.EDProducer('CTPPSPixelClusterProducer',
    RPixVerbosity = cms.untracked.int32(0),
    tag = cms.InputTag('ctppsPixelDigis'),
    SeedADCThreshold = cms.int32(2),
    ADCThreshold = cms.int32(2),
    ElectronADCGain = cms.double(135),
    VCaltoElectronGain = cms.int32(50),
    VCaltoElectronOffset = cms.int32(-411),
    doSingleCalibration = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

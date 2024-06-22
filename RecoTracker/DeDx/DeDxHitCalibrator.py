import FWCore.ParameterSet.Config as cms

def DeDxHitCalibrator(**kwargs):
  mod = cms.EDProducer('DeDxHitCalibrator',
    applyGain = cms.bool(True),
    MeVPerElectron = cms.double(3.61e-06),
    VCaltoElectronGain = cms.int32(65),
    VCaltoElectronGain_L1 = cms.int32(65),
    VCaltoElectronOffset = cms.int32(-414),
    VCaltoElectronOffset_L1 = cms.int32(-414),
    pixelSaturationThr = cms.int32(254),
    trackProducer = cms.InputTag('generalTracks'),
    dedxHitInfo = cms.InputTag('dedxHitInfo'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

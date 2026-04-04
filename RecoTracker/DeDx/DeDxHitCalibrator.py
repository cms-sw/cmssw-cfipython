import FWCore.ParameterSet.Config as cms

def DeDxHitCalibrator(*args, **kwargs):
  mod = cms.EDProducer('DeDxHitCalibrator',
    applyGain = cms.bool(True),
    MeVPerElectron = cms.double(3.61e-06),
    trackProducer = cms.InputTag('generalTracks'),
    dedxHitInfo = cms.InputTag('dedxHitInfo'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

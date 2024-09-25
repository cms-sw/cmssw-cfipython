import FWCore.ParameterSet.Config as cms

def HLTHcalLaserMisfireFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTHcalLaserMisfireFilter',
    InputHBHE = cms.InputTag('source'),
    InputHF = cms.InputTag('source'),
    minADCHBHE = cms.int32(10),
    minADCHF = cms.int32(10),
    minFracDiffHBHELaser = cms.double(0.3),
    minFracHFLaser = cms.double(0.3),
    testMode = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

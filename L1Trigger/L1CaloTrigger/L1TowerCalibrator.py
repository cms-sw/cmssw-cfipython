import FWCore.ParameterSet.Config as cms

def L1TowerCalibrator(**kwargs):
  mod = cms.EDProducer('L1TowerCalibrator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ExpoRandomPtGunProducer(**kwargs):
  mod = cms.EDProducer('ExpoRandomPtGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

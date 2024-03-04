import FWCore.ParameterSet.Config as cms

def ExpoRandomPGunProducer(**kwargs):
  mod = cms.EDProducer('ExpoRandomPGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ExpoRandomPtGunProducer(*args, **kwargs):
  mod = cms.EDProducer('ExpoRandomPtGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

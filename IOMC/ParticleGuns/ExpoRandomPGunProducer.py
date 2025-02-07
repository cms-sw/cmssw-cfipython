import FWCore.ParameterSet.Config as cms

def ExpoRandomPGunProducer(*args, **kwargs):
  mod = cms.EDProducer('ExpoRandomPGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def FlatRandomEGunProducer(*args, **kwargs):
  mod = cms.EDProducer('FlatRandomEGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

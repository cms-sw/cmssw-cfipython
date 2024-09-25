import FWCore.ParameterSet.Config as cms

def FlatRandomPtGunProducer(*args, **kwargs):
  mod = cms.EDProducer('FlatRandomPtGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

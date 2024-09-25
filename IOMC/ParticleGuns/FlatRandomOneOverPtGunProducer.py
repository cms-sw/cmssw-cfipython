import FWCore.ParameterSet.Config as cms

def FlatRandomOneOverPtGunProducer(*args, **kwargs):
  mod = cms.EDProducer('FlatRandomOneOverPtGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

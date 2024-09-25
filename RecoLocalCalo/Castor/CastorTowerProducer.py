import FWCore.ParameterSet.Config as cms

def CastorTowerProducer(*args, **kwargs):
  mod = cms.EDProducer('CastorTowerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

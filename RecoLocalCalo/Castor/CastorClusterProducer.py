import FWCore.ParameterSet.Config as cms

def CastorClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('CastorClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

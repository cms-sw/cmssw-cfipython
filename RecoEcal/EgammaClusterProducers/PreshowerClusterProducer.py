import FWCore.ParameterSet.Config as cms

def PreshowerClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('PreshowerClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

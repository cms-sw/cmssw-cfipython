import FWCore.ParameterSet.Config as cms

def HybridClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('HybridClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

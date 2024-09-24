import FWCore.ParameterSet.Config as cms

def Multi5x5ClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('Multi5x5ClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

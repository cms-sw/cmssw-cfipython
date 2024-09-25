import FWCore.ParameterSet.Config as cms

def ShallowClustersProducer(*args, **kwargs):
  mod = cms.EDProducer('ShallowClustersProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

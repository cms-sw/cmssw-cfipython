import FWCore.ParameterSet.Config as cms

def ShallowRechitClustersProducer(*args, **kwargs):
  mod = cms.EDProducer('ShallowRechitClustersProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ShallowSimhitClustersProducer(*args, **kwargs):
  mod = cms.EDProducer('ShallowSimhitClustersProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

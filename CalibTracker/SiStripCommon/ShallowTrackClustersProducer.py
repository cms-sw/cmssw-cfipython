import FWCore.ParameterSet.Config as cms

def ShallowTrackClustersProducer(*args, **kwargs):
  mod = cms.EDProducer('ShallowTrackClustersProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

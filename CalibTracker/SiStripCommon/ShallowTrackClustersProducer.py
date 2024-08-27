import FWCore.ParameterSet.Config as cms

def ShallowTrackClustersProducer(**kwargs):
  mod = cms.EDProducer('ShallowTrackClustersProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

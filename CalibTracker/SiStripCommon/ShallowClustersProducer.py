import FWCore.ParameterSet.Config as cms

def ShallowClustersProducer(**kwargs):
  mod = cms.EDProducer('ShallowClustersProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

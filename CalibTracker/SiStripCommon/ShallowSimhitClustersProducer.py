import FWCore.ParameterSet.Config as cms

def ShallowSimhitClustersProducer(**kwargs):
  mod = cms.EDProducer('ShallowSimhitClustersProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

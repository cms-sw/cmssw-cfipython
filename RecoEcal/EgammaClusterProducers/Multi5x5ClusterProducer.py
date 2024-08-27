import FWCore.ParameterSet.Config as cms

def Multi5x5ClusterProducer(**kwargs):
  mod = cms.EDProducer('Multi5x5ClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

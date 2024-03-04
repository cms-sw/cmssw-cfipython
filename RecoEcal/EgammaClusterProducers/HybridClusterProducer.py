import FWCore.ParameterSet.Config as cms

def HybridClusterProducer(**kwargs):
  mod = cms.EDProducer('HybridClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

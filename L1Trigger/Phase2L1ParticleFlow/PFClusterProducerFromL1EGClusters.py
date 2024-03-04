import FWCore.ParameterSet.Config as cms

def PFClusterProducerFromL1EGClusters(**kwargs):
  mod = cms.EDProducer('PFClusterProducerFromL1EGClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PFClusterProducerFromHGC3DClusters(**kwargs):
  mod = cms.EDProducer('PFClusterProducerFromHGC3DClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def PFClusterProducerFromL1EGClusters(*args, **kwargs):
  mod = cms.EDProducer('PFClusterProducerFromL1EGClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

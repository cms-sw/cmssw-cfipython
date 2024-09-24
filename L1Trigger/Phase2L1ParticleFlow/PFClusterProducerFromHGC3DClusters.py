import FWCore.ParameterSet.Config as cms

def PFClusterProducerFromHGC3DClusters(*args, **kwargs):
  mod = cms.EDProducer('PFClusterProducerFromHGC3DClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

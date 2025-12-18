import FWCore.ParameterSet.Config as cms

def PFClusterCollectionMerger(*args, **kwargs):
  mod = cms.EDProducer('PFClusterCollectionMerger',
    inputs = cms.VInputTag(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

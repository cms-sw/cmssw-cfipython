import FWCore.ParameterSet.Config as cms

def PFClusterCollectionMerger(**kwargs):
  mod = cms.EDProducer('PFClusterCollectionMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

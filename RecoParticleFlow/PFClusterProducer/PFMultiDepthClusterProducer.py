import FWCore.ParameterSet.Config as cms

def PFMultiDepthClusterProducer(**kwargs):
  mod = cms.EDProducer('PFMultiDepthClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

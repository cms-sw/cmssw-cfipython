import FWCore.ParameterSet.Config as cms

def trgMatchedSuperClusterProducer(**kwargs):
  mod = cms.EDProducer('trgMatchedSuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

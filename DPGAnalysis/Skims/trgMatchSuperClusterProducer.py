import FWCore.ParameterSet.Config as cms

def trgMatchSuperClusterProducer(**kwargs):
  mod = cms.EDProducer('trgMatchSuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

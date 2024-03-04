import FWCore.ParameterSet.Config as cms

def Multi5x5SuperClusterProducer(**kwargs):
  mod = cms.EDProducer('Multi5x5SuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

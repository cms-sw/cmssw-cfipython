import FWCore.ParameterSet.Config as cms

def ClusterCompatibilityProducer(**kwargs):
  mod = cms.EDProducer('ClusterCompatibilityProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

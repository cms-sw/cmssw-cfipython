import FWCore.ParameterSet.Config as cms

def ClusterCount(**kwargs):
  mod = cms.EDProducer('ClusterCount',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

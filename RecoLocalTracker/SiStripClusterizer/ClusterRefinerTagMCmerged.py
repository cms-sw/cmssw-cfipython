import FWCore.ParameterSet.Config as cms

def ClusterRefinerTagMCmerged(**kwargs):
  mod = cms.EDProducer('ClusterRefinerTagMCmerged',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def HITrackClusterRemover(**kwargs):
  mod = cms.EDProducer('HITrackClusterRemover',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def TracksToTrajectories(**kwargs):
  mod = cms.EDProducer('TracksToTrajectories',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

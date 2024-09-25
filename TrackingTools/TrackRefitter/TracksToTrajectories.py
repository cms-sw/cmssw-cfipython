import FWCore.ParameterSet.Config as cms

def TracksToTrajectories(*args, **kwargs):
  mod = cms.EDProducer('TracksToTrajectories',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

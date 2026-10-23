import FWCore.ParameterSet.Config as cms

def GenTrackMatcher(*args, **kwargs):
  mod = cms.EDProducer('GenTrackMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

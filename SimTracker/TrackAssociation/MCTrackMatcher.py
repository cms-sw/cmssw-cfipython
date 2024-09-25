import FWCore.ParameterSet.Config as cms

def MCTrackMatcher(*args, **kwargs):
  mod = cms.EDProducer('MCTrackMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

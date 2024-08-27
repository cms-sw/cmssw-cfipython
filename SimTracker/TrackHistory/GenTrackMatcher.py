import FWCore.ParameterSet.Config as cms

def GenTrackMatcher(**kwargs):
  mod = cms.EDProducer('GenTrackMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

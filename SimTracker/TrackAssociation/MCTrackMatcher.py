import FWCore.ParameterSet.Config as cms

def MCTrackMatcher(**kwargs):
  mod = cms.EDProducer('MCTrackMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

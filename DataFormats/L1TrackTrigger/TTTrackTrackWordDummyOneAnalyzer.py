import FWCore.ParameterSet.Config as cms

def TTTrackTrackWordDummyOneAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TTTrackTrackWordDummyOneAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

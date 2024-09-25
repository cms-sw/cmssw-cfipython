import FWCore.ParameterSet.Config as cms

def PatTrackAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatTrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

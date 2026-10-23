import FWCore.ParameterSet.Config as cms

def myTrackAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('myTrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

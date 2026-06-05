import FWCore.ParameterSet.Config as cms

def TrackHistoryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackHistoryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

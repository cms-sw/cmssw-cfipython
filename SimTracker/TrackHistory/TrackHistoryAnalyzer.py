import FWCore.ParameterSet.Config as cms

def TrackHistoryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackHistoryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

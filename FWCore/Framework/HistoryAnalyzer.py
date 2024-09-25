import FWCore.ParameterSet.Config as cms

def HistoryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HistoryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

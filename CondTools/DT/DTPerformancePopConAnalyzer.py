import FWCore.ParameterSet.Config as cms

def DTPerformancePopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DTPerformancePopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

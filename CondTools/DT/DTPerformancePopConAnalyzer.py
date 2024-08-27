import FWCore.ParameterSet.Config as cms

def DTPerformancePopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTPerformancePopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

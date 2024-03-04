import FWCore.ParameterSet.Config as cms

def DTRangeT0PopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTRangeT0PopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

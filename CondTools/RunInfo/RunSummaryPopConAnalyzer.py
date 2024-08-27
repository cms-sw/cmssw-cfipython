import FWCore.ParameterSet.Config as cms

def RunSummaryPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RunSummaryPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def RunSummaryESAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RunSummaryESAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

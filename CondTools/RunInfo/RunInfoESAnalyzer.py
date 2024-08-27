import FWCore.ParameterSet.Config as cms

def RunInfoESAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RunInfoESAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def LHCInfoPerFillAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerFillAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

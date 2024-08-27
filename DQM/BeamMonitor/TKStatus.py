import FWCore.ParameterSet.Config as cms

def TKStatus(**kwargs):
  mod = cms.EDAnalyzer('TKStatus',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

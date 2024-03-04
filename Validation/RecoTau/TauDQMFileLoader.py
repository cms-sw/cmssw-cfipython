import FWCore.ParameterSet.Config as cms

def TauDQMFileLoader(**kwargs):
  mod = cms.EDAnalyzer('TauDQMFileLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

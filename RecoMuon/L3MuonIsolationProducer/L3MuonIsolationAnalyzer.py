import FWCore.ParameterSet.Config as cms

def L3MuonIsolationAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L3MuonIsolationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

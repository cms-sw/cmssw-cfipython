import FWCore.ParameterSet.Config as cms

def L2MuonIsolationAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L2MuonIsolationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

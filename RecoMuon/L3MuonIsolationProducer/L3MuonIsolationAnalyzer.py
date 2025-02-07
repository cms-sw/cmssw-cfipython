import FWCore.ParameterSet.Config as cms

def L3MuonIsolationAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('L3MuonIsolationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

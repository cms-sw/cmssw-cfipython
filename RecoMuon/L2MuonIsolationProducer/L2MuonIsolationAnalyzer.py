import FWCore.ParameterSet.Config as cms

def L2MuonIsolationAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('L2MuonIsolationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

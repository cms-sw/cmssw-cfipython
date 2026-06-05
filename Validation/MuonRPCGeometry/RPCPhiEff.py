import FWCore.ParameterSet.Config as cms

def RPCPhiEff(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCPhiEff',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

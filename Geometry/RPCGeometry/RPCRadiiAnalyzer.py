import FWCore.ParameterSet.Config as cms

def RPCRadiiAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCRadiiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

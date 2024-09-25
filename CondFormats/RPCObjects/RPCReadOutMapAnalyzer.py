import FWCore.ParameterSet.Config as cms

def RPCReadOutMapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCReadOutMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

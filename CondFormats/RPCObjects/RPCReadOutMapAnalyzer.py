import FWCore.ParameterSet.Config as cms

def RPCReadOutMapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RPCReadOutMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

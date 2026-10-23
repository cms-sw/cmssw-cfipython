import FWCore.ParameterSet.Config as cms

def RPCPopConObPVSSmapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCPopConObPVSSmapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

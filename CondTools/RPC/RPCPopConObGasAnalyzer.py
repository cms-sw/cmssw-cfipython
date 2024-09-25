import FWCore.ParameterSet.Config as cms

def RPCPopConObGasAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCPopConObGasAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

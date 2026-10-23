import FWCore.ParameterSet.Config as cms

def RPCPopConObUXCAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCPopConObUXCAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def RPCPopConObFebmapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCPopConObFebmapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

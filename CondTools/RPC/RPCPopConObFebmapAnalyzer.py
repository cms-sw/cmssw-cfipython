import FWCore.ParameterSet.Config as cms

def RPCPopConObFebmapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RPCPopConObFebmapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def RPCGEO(**kwargs):
  mod = cms.EDAnalyzer('RPCGEO',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

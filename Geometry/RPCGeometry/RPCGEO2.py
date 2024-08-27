import FWCore.ParameterSet.Config as cms

def RPCGEO2(**kwargs):
  mod = cms.EDAnalyzer('RPCGEO2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

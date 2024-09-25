import FWCore.ParameterSet.Config as cms

def RPCGEO(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCGEO',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def RPCRadiiAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RPCRadiiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

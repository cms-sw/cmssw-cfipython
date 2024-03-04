import FWCore.ParameterSet.Config as cms

def RPCGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RPCGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

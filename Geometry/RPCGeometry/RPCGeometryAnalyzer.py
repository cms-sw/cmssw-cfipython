import FWCore.ParameterSet.Config as cms

def RPCGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

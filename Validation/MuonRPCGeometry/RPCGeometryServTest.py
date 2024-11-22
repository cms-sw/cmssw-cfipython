import FWCore.ParameterSet.Config as cms

def RPCGeometryServTest(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCGeometryServTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

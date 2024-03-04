import FWCore.ParameterSet.Config as cms

def RPCGeometryServTest(**kwargs):
  mod = cms.EDAnalyzer('RPCGeometryServTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

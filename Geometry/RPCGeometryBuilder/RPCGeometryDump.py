import FWCore.ParameterSet.Config as cms

def RPCGeometryDump(**kwargs):
  mod = cms.EDAnalyzer('RPCGeometryDump',
    verbose = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

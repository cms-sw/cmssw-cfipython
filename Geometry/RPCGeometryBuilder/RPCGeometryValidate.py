import FWCore.ParameterSet.Config as cms

def RPCGeometryValidate(**kwargs):
  mod = cms.EDAnalyzer('RPCGeometryValidate',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

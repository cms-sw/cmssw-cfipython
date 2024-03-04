import FWCore.ParameterSet.Config as cms

def ROCmTestOpaqueAdditionModule(**kwargs):
  mod = cms.EDAnalyzer('ROCmTestOpaqueAdditionModule',
    size = cms.uint32(1048576),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

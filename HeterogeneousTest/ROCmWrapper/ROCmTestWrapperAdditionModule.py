import FWCore.ParameterSet.Config as cms

def ROCmTestWrapperAdditionModule(**kwargs):
  mod = cms.EDAnalyzer('ROCmTestWrapperAdditionModule',
    size = cms.uint32(1048576),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

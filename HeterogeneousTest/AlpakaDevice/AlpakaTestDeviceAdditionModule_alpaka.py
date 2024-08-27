import FWCore.ParameterSet.Config as cms

def AlpakaTestDeviceAdditionModule_alpaka(**kwargs):
  mod = cms.EDAnalyzer('AlpakaTestDeviceAdditionModule@alpaka',
    size = cms.uint32(1048576),
    alpaka = cms.untracked.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

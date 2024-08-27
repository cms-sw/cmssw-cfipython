import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_AlpakaTestWrapperAdditionModule(**kwargs):
  mod = cms.EDAnalyzer('alpaka_serial_sync::AlpakaTestWrapperAdditionModule',
    size = cms.uint32(1048576),
    alpaka = cms.untracked.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

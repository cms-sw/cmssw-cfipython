import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_AlpakaTestOpaqueAdditionModule(*args, **kwargs):
  mod = cms.EDAnalyzer('alpaka_serial_sync::AlpakaTestOpaqueAdditionModule',
    size = cms.uint32(1048576),
    alpaka = cms.untracked.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

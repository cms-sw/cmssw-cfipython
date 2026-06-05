import FWCore.ParameterSet.Config as cms

def AlignmentCSCOverlapSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentCSCOverlapSelectorModule',
    src = cms.InputTag(''),
    station = cms.int32(1),
    minHitsPerChamber = cms.uint32(0),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

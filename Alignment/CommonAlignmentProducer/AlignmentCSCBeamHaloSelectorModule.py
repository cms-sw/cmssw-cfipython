import FWCore.ParameterSet.Config as cms

def AlignmentCSCBeamHaloSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentCSCBeamHaloSelectorModule',
    src = cms.InputTag(''),
    minStations = cms.uint32(0),
    minHitsPerStation = cms.uint32(1),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

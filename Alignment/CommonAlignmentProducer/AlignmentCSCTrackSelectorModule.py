import FWCore.ParameterSet.Config as cms

def AlignmentCSCTrackSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentCSCTrackSelectorModule',
    src = cms.InputTag(''),
    stationA = cms.int32(0),
    stationB = cms.int32(0),
    minHitsDT = cms.int32(0),
    minHitsPerStation = cms.int32(0),
    maxHitsPerStation = cms.int32(0),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

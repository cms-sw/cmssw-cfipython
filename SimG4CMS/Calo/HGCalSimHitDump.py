import FWCore.ParameterSet.Config as cms

def HGCalSimHitDump(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalSimHitDump',
    ModuleLabel = cms.string('g4SimHits'),
    HitCollections = cms.vstring(
      'HGCHitsEE',
      'CalibrationHGCHitsEE',
      'HGCHitsHEfront',
      'CalibrationHGCHitsHEfront',
      'HGCHitsHEback',
      'CalibrationHGCHitsHEback'
    ),
    CollectionTypes = cms.vint32(
      0,
      0,
      0,
      0,
      1,
      1
    ),
    MaxEvent = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

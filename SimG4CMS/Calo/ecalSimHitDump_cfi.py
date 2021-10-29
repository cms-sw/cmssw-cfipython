import FWCore.ParameterSet.Config as cms

ecalSimHitDump = cms.EDAnalyzer('EcalSimHitDump',
  ModuleLabel = cms.string('g4SimHits'),
  HitCollections = cms.vstring(
    'EcalHitsEB',
    'EcalHitsEE',
    'EcalHitsES'
  ),
  CollectionTypes = cms.vint32(
    0,
    1,
    2
  ),
  MaxEvent = cms.int32(10),
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

muonSimHitDump = cms.EDAnalyzer('MuonSimHitDump',
  ModuleLabel = cms.string('g4SimHits'),
  HitCollections = cms.vstring(
    'MuonDTHits',
    'MuonCSCHits',
    'MuonRPCHits',
    'MuonGEMHits'
  ),
  CollectionTypes = cms.vint32(
    0,
    1,
    2,
    3
  ),
  MaxEvent = cms.int32(10),
  mightGet = cms.optional.untracked.vstring
)

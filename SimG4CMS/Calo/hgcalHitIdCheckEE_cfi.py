import FWCore.ParameterSet.Config as cms

hgcalHitIdCheckEE = cms.EDAnalyzer('HGcalHitIdCheck',
  moduleLabel = cms.string('g4SimHits'),
  caloHitSource = cms.string('HGCHitsEE'),
  nameSense = cms.string('HGCalEESensitive'),
  nameDevice = cms.string('HGCal EE'),
  Verbosity = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)

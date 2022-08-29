import FWCore.ParameterSet.Config as cms

hgcalHitScintillator = cms.EDAnalyzer('HGCalTestScintHits',
  moduleLabel = cms.string('g4SimHits'),
  caloHitSource = cms.string('HGCHitsHEback'),
  nameSense = cms.string('HGCalHEScintillatorSensitive'),
  tileFileName = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

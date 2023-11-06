import FWCore.ParameterSet.Config as cms

hgcalHitPartialEE = cms.EDAnalyzer('HGCalTestPartialWaferHits',
  moduleLabel = cms.string('g4SimHits'),
  caloHitSource = cms.string('HGCHitsEE'),
  nameSense = cms.string('HGCalEESensitive'),
  missingFile = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

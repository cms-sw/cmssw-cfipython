import FWCore.ParameterSet.Config as cms

hgcalHitPartialEE = cms.EDAnalyzer('HGCalHitPartial',
  moduleLabel = cms.string('g4SimHits'),
  caloHitSource = cms.string('HGCHitsEE'),
  nameSense = cms.string('HGCalEESensitive'),
  mightGet = cms.optional.untracked.vstring
)

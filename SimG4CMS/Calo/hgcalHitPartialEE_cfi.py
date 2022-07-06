import FWCore.ParameterSet.Config as cms

hgcalHitPartialEE = cms.EDAnalyzer('HGcalHitPartial',
  moduleLabel = cms.string('g4SimHits'),
  caloHitSource = cms.string('HGCHitsEE'),
  nameSense = cms.string('HGCalEESensitive'),
  mightGet = cms.optional.untracked.vstring
)

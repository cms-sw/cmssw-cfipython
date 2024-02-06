import FWCore.ParameterSet.Config as cms

hgcalToolTesterPartialWaferEE = cms.EDAnalyzer('HGCalToolTesterPartialWafer',
  moduleLabel = cms.string('g4SimHits'),
  caloHitSource = cms.string('HGCHitsEE'),
  nameSense = cms.string('HGCalEESensitive'),
  mightGet = cms.optional.untracked.vstring
)

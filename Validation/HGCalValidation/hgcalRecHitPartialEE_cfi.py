import FWCore.ParameterSet.Config as cms

hgcalRecHitPartialEE = cms.EDAnalyzer('HGCalTestPartialWaferRecHits',
  detectorName = cms.string('HGCalEESensitive'),
  missingFile = cms.string(''),
  source = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  mightGet = cms.optional.untracked.vstring
)

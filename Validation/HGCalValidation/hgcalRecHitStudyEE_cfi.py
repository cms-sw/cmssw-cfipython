import FWCore.ParameterSet.Config as cms

hgcalRecHitStudyEE = cms.EDAnalyzer('HGCalRecHitStudy',
  DetectorName = cms.string('HGCalEESensitive'),
  RecHitSource = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  ifHCAL = cms.bool(False),
  Verbosity = cms.untracked.int32(0)
)

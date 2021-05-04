import FWCore.ParameterSet.Config as cms

hgcalRecHitValidationEE = cms.EDProducer('HGCalRecHitValidation',
  DetectorName = cms.string('HGCalEESensitive'),
  RecHitSource = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  Verbosity = cms.untracked.int32(0),
  mightGet = cms.optional.untracked.vstring
)

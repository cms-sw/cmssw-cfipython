import FWCore.ParameterSet.Config as cms

ecalAnalFitUncalibRecHit = cms.EDProducer('EcalUncalibRecHitProducer',
  EBdigiCollection = cms.InputTag('ecalDigis', 'ebDigis'),
  EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
  EEdigiCollection = cms.InputTag('ecalDigis', 'eeDigis'),
  EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
  algo = cms.string('EcalUncalibRecHitWorkerAnalFit'),
  algoPSet = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)

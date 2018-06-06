import FWCore.ParameterSet.Config as cms

ecalFixedAlphaBetaFitUncalibRecHit = cms.EDProducer('EcalUncalibRecHitProducer',
  EBdigiCollection = cms.InputTag('ecalDigis', 'ebDigis'),
  EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
  EEdigiCollection = cms.InputTag('ecalDigis', 'eeDigis'),
  EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
  algo = cms.string('EcalUncalibRecHitWorkerFixedAlphaBetaFit'),
  algoPSet = cms.PSet(
    alphaEB = cms.double(1.138),
    alphaEE = cms.double(1.89),
    AlphaBetaFilename = cms.untracked.string('NOFILE'),
    betaEB = cms.double(1.655),
    MinAmplEndcap = cms.double(14),
    MinAmplBarrel = cms.double(8),
    betaEE = cms.double(1.4),
    UseDynamicPedestal = cms.bool(True)
  )
)

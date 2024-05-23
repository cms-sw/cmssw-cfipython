import FWCore.ParameterSet.Config as cms

from .EcalUncalibRecHitProducer import EcalUncalibRecHitProducer

ecalFixedAlphaBetaFitUncalibRecHitProducer = EcalUncalibRecHitProducer(
  EBdigiCollection = ('ecalDigis', 'ebDigis'),
  EEhitCollection = 'EcalUncalibRecHitsEE',
  EEdigiCollection = ('ecalDigis', 'eeDigis'),
  EBhitCollection = 'EcalUncalibRecHitsEB',
  algo = 'EcalUncalibRecHitWorkerFixedAlphaBetaFit',
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

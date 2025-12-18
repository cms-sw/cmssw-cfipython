import FWCore.ParameterSet.Config as cms

from .EcalUncalibRecHitProducer import EcalUncalibRecHitProducer

ecalWeightsUncalibRecHitProducer = EcalUncalibRecHitProducer(
  EBdigiCollection = ('ecalDigis', 'ebDigis'),
  EEhitCollection = 'EcalUncalibRecHitsEE',
  EEdigiCollection = ('ecalDigis', 'eeDigis'),
  EBhitCollection = 'EcalUncalibRecHitsEB',
  algo = 'EcalUncalibRecHitWorkerWeights',
  algoPSet = cms.PSet()
)

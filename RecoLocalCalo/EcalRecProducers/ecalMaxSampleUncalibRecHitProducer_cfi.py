import FWCore.ParameterSet.Config as cms

from .EcalUncalibRecHitProducer import EcalUncalibRecHitProducer

ecalMaxSampleUncalibRecHitProducer = EcalUncalibRecHitProducer(
  EBdigiCollection = ('ecalDigis', 'ebDigis'),
  EEhitCollection = 'EcalUncalibRecHitsEE',
  EEdigiCollection = ('ecalDigis', 'eeDigis'),
  EBhitCollection = 'EcalUncalibRecHitsEB',
  algo = 'EcalUncalibRecHitWorkerMaxSample',
  algoPSet = cms.PSet()
)

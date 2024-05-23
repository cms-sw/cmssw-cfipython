import FWCore.ParameterSet.Config as cms

from .EcalUncalibRecHitProducer import EcalUncalibRecHitProducer

ecalAnalFitUncalibRecHitProducer = EcalUncalibRecHitProducer(
  EBdigiCollection = ('ecalDigis', 'ebDigis'),
  EEhitCollection = 'EcalUncalibRecHitsEE',
  EEdigiCollection = ('ecalDigis', 'eeDigis'),
  EBhitCollection = 'EcalUncalibRecHitsEB',
  algo = 'EcalUncalibRecHitWorkerAnalFit',
  algoPSet = cms.PSet()
)

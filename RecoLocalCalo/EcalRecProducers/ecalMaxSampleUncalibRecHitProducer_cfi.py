import FWCore.ParameterSet.Config as cms

from .EcalUncalibRecHitProducer import EcalUncalibRecHitProducer

ecalMaxSampleUncalibRecHitProducer = EcalUncalibRecHitProducer(

  algo = 'EcalUncalibRecHitWorkerMaxSample',
  algoPSet = cms.PSet()
)

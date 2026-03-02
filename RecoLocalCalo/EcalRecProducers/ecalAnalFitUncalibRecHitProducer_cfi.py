import FWCore.ParameterSet.Config as cms

from .EcalUncalibRecHitProducer import EcalUncalibRecHitProducer

ecalAnalFitUncalibRecHitProducer = EcalUncalibRecHitProducer(

  algo = 'EcalUncalibRecHitWorkerAnalFit',
  algoPSet = cms.PSet()
)

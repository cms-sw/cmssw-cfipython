import FWCore.ParameterSet.Config as cms

from .EcalUncalibRecHitProducer import EcalUncalibRecHitProducer

ecalWeightsUncalibRecHitProducer = EcalUncalibRecHitProducer(

  algo = 'EcalUncalibRecHitWorkerWeights',
  algoPSet = cms.PSet()
)

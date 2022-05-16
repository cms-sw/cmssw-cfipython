import FWCore.ParameterSet.Config as cms

ecalCPUUncalibRecHitProducer = cms.EDProducer('EcalCPUUncalibRecHitProducer',
  recHitsInLabelEB = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEB'),
  recHitsInLabelEE = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEE'),
  recHitsOutLabelEB = cms.string('EcalUncalibRecHitsEB'),
  recHitsOutLabelEE = cms.string('EcalUncalibRecHitsEE'),
  containsTimingInformation = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

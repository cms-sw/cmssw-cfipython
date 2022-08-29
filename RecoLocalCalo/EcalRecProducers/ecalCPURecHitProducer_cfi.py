import FWCore.ParameterSet.Config as cms

ecalCPURecHitProducer = cms.EDProducer('EcalCPURecHitProducer',
  recHitsInLabelEB = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsEB'),
  recHitsInLabelEE = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsEE'),
  recHitsOutLabelEB = cms.string('EcalRecHitsEB'),
  recHitsOutLabelEE = cms.string('EcalRecHitsEE'),
  containsTimingInformation = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

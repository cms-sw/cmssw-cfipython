import FWCore.ParameterSet.Config as cms

ecalRecHitConvertGPU2CPUFormat = cms.EDProducer('EcalRecHitConvertGPU2CPUFormat',
  recHitsLabelGPUEB = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsGPUEB'),
  recHitsLabelGPUEE = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsGPUEE'),
  recHitsLabelCPUEB = cms.string('EcalRecHitsEB'),
  recHitsLabelCPUEE = cms.string('EcalRecHitsEE'),
  mightGet = cms.optional.untracked.vstring
)

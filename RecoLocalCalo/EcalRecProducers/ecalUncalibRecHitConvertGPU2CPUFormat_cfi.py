import FWCore.ParameterSet.Config as cms

ecalUncalibRecHitConvertGPU2CPUFormat = cms.EDProducer('EcalUncalibRecHitConvertGPU2CPUFormat',
  recHitsLabelGPUEB = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEB'),
  recHitsLabelGPUEE = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEE'),
  recHitsLabelCPUEB = cms.string('EcalUncalibRecHitsEB'),
  recHitsLabelCPUEE = cms.string('EcalUncalibRecHitsEE'),
  mightGet = cms.optional.untracked.vstring
)

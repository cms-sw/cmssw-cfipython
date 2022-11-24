import FWCore.ParameterSet.Config as cms

ecalUncalibRecHitConvertGPU2CPUFormat = cms.EDProducer('EcalUncalibRecHitConvertGPU2CPUFormat',
  recHitsLabelGPUEB = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEB'),
  recHitsLabelCPUEB = cms.string('EcalUncalibRecHitsEB'),
  isPhase2 = cms.bool(False),
  recHitsLabelGPUEE = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEE'),
  recHitsLabelCPUEE = cms.string('EcalUncalibRecHitsEE'),
  mightGet = cms.optional.untracked.vstring
)

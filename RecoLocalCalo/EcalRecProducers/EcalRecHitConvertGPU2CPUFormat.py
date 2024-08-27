import FWCore.ParameterSet.Config as cms

def EcalRecHitConvertGPU2CPUFormat(**kwargs):
  mod = cms.EDProducer('EcalRecHitConvertGPU2CPUFormat',
    recHitsLabelGPUEB = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsGPUEB'),
    recHitsLabelGPUEE = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsGPUEE'),
    recHitsLabelCPUEB = cms.string('EcalRecHitsEB'),
    recHitsLabelCPUEE = cms.string('EcalRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

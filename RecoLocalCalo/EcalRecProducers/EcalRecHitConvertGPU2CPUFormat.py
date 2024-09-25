import FWCore.ParameterSet.Config as cms

def EcalRecHitConvertGPU2CPUFormat(*args, **kwargs):
  mod = cms.EDProducer('EcalRecHitConvertGPU2CPUFormat',
    recHitsLabelGPUEB = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsGPUEB'),
    recHitsLabelGPUEE = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsGPUEE'),
    recHitsLabelCPUEB = cms.string('EcalRecHitsEB'),
    recHitsLabelCPUEE = cms.string('EcalRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

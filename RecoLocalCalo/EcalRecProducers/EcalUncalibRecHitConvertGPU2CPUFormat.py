import FWCore.ParameterSet.Config as cms

def EcalUncalibRecHitConvertGPU2CPUFormat(*args, **kwargs):
  mod = cms.EDProducer('EcalUncalibRecHitConvertGPU2CPUFormat',
    recHitsLabelGPUEB = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEB'),
    recHitsLabelCPUEB = cms.string('EcalUncalibRecHitsEB'),
    isPhase2 = cms.bool(False),
    recHitsLabelGPUEE = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEE'),
    recHitsLabelCPUEE = cms.string('EcalUncalibRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

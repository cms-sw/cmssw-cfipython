import FWCore.ParameterSet.Config as cms

def EcalCPURecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalCPURecHitProducer',
    recHitsInLabelEB = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsEB'),
    recHitsInLabelEE = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsEE'),
    recHitsOutLabelEB = cms.string('EcalRecHitsEB'),
    recHitsOutLabelEE = cms.string('EcalRecHitsEE'),
    containsTimingInformation = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

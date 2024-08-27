import FWCore.ParameterSet.Config as cms

def EcalCPURecHitProducer(**kwargs):
  mod = cms.EDProducer('EcalCPURecHitProducer',
    recHitsInLabelEB = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsEB'),
    recHitsInLabelEE = cms.InputTag('ecalRecHitProducerGPU', 'EcalRecHitsEE'),
    recHitsOutLabelEB = cms.string('EcalRecHitsEB'),
    recHitsOutLabelEE = cms.string('EcalRecHitsEE'),
    containsTimingInformation = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

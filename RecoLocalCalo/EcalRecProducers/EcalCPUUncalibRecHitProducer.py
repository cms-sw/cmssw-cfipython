import FWCore.ParameterSet.Config as cms

def EcalCPUUncalibRecHitProducer(**kwargs):
  mod = cms.EDProducer('EcalCPUUncalibRecHitProducer',
    recHitsInLabelEB = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEB'),
    recHitsOutLabelEB = cms.string('EcalUncalibRecHitsEB'),
    containsTimingInformation = cms.bool(False),
    isPhase2 = cms.bool(False),
    recHitsInLabelEE = cms.InputTag('ecalUncalibRecHitProducerGPU', 'EcalUncalibRecHitsEE'),
    recHitsOutLabelEE = cms.string('EcalUncalibRecHitsEE'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

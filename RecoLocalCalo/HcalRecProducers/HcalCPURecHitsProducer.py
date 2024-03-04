import FWCore.ParameterSet.Config as cms

def HcalCPURecHitsProducer(**kwargs):
  mod = cms.EDProducer('HcalCPURecHitsProducer',
    recHitsM0LabelIn = cms.InputTag('hbheRecHitProducerGPU'),
    recHitsM0LabelOut = cms.string(''),
    recHitsLegacyLabelOut = cms.string(''),
    produceSoA = cms.bool(True),
    produceLegacy = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

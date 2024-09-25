import FWCore.ParameterSet.Config as cms

def HcalCPURecHitsProducer(*args, **kwargs):
  mod = cms.EDProducer('HcalCPURecHitsProducer',
    recHitsM0LabelIn = cms.InputTag('hbheRecHitProducerGPU'),
    recHitsM0LabelOut = cms.string(''),
    recHitsLegacyLabelOut = cms.string(''),
    produceSoA = cms.bool(True),
    produceLegacy = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def HcalDigisProducerGPU(*args, **kwargs):
  mod = cms.EDProducer('HcalDigisProducerGPU',
    hbheDigisLabel = cms.InputTag('hcalDigis'),
    qie11DigiLabel = cms.InputTag('hcalDigis'),
    digisLabelF01HE = cms.string('f01HEDigisGPU'),
    digisLabelF5HB = cms.string('f5HBDigisGPU'),
    digisLabelF3HB = cms.string('f3HBDigisGPU'),
    maxChannelsF01HE = cms.uint32(10000),
    maxChannelsF5HB = cms.uint32(10000),
    maxChannelsF3HB = cms.uint32(10000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

hcalDigisProducerGPU = cms.EDProducer('HcalDigisProducerGPU',
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

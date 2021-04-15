import FWCore.ParameterSet.Config as cms

hcalCPUDigisProducer = cms.EDProducer('HcalCPUDigisProducer',
  digisLabelF01HEIn = cms.InputTag('hcalRawToDigiGPU', 'f01HEDigisGPU'),
  digisLabelF5HBIn = cms.InputTag('hcalRawToDigiGPU', 'f5HBDigisGPU'),
  digisLabelF3HBIn = cms.InputTag('hcalRawToDigiGPU', 'f3HBDigisGPU'),
  digisLabelF01HEOut = cms.string('f01HEDigis'),
  digisLabelF5HBOut = cms.string('f5HBDigis'),
  digisLabelF3HBOut = cms.string('f3HBDigis'),
  mightGet = cms.optional.untracked.vstring
)

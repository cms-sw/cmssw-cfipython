import FWCore.ParameterSet.Config as cms

def EcalCPUDigisProducer(**kwargs):
  mod = cms.EDProducer('EcalCPUDigisProducer',
    digisInLabelEB = cms.InputTag('ecalRawToDigiGPU', 'ebDigis'),
    digisInLabelEE = cms.InputTag('ecalRawToDigiGPU', 'eeDigis'),
    digisOutLabelEB = cms.string('ebDigis'),
    digisOutLabelEE = cms.string('eeDigis'),
    produceDummyIntegrityCollections = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

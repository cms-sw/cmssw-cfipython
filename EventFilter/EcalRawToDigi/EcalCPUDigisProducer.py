import FWCore.ParameterSet.Config as cms

def EcalCPUDigisProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalCPUDigisProducer',
    digisInLabelEB = cms.InputTag('ecalRawToDigiGPU', 'ebDigis'),
    digisInLabelEE = cms.InputTag('ecalRawToDigiGPU', 'eeDigis'),
    digisOutLabelEB = cms.string('ebDigis'),
    digisOutLabelEE = cms.string('eeDigis'),
    produceDummyIntegrityCollections = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

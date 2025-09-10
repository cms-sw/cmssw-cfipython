import FWCore.ParameterSet.Config as cms

def EcalDigisFromPortableProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalDigisFromPortableProducer',
    digisInLabelEB = cms.InputTag('ecalRawToDigiPortable', 'ebDigis'),
    digisInLabelEE = cms.InputTag('ecalRawToDigiPortable', 'eeDigis'),
    digisOutLabelEB = cms.string('ebDigis'),
    digisOutLabelEE = cms.string('eeDigis'),
    produceDummyIntegrityCollections = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

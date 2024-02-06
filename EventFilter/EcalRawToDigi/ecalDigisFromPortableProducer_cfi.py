import FWCore.ParameterSet.Config as cms

ecalDigisFromPortableProducer = cms.EDProducer('EcalDigisFromPortableProducer',
  digisInLabelEB = cms.InputTag('ecalRawToDigiPortable', 'ebDigis'),
  digisInLabelEE = cms.InputTag('ecalRawToDigiPortable', 'eeDigis'),
  digisOutLabelEB = cms.string('ebDigis'),
  digisOutLabelEE = cms.string('eeDigis'),
  produceDummyIntegrityCollections = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)

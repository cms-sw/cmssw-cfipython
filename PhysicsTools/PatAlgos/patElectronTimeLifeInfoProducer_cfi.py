import FWCore.ParameterSet.Config as cms

patElectronTimeLifeInfoProducer = cms.EDProducer('PATElectronTimeLifeInfoProducer',
  src = cms.InputTag('slimmedElectrons'),
  pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
  selection = cms.string(''),
  pvChoice = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)

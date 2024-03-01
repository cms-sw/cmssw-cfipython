import FWCore.ParameterSet.Config as cms

patTauTimeLifeInfoProducer = cms.EDProducer('PATTauTimeLifeInfoProducer',
  src = cms.InputTag('slimmedTaus'),
  pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
  selection = cms.string(''),
  pvChoice = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)

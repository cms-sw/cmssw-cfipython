import FWCore.ParameterSet.Config as cms

patMuonTimeLifeInfoProducer = cms.EDProducer('PATMuonTimeLifeInfoProducer',
  src = cms.InputTag('slimmedMuons'),
  pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
  selection = cms.string(''),
  pvChoice = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)

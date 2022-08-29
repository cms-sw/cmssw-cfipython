import FWCore.ParameterSet.Config as cms

muonIDTable = cms.EDProducer('MuonIDTableProducer',
  muons = cms.required.InputTag,
  vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
  name = cms.required.string,
  mightGet = cms.optional.untracked.vstring
)

import FWCore.ParameterSet.Config as cms

muonFSRAssociator = cms.EDProducer('MuonFSRAssociator',
  photons = cms.required.InputTag,
  muons = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)

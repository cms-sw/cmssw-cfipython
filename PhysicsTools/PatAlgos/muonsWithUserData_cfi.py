import FWCore.ParameterSet.Config as cms

muonsWithUserData = cms.EDProducer('PATMuonUserDataEmbedder',
  src = cms.required.InputTag,
  parentSrcs = cms.VInputTag(),
  userFloats = cms.PSet(),
  userInts = cms.PSet(),
  userIntFromBools = cms.PSet(),
  userCands = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)

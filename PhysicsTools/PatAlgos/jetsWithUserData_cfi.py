import FWCore.ParameterSet.Config as cms

jetsWithUserData = cms.EDProducer('PATJetUserDataEmbedder',
  userFloats = cms.PSet(),
  userInts = cms.PSet(),
  userIntFromBools = cms.PSet(),
  userCands = cms.PSet()
)

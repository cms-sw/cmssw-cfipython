import FWCore.ParameterSet.Config as cms

muonsWithUserData = cms.EDProducer('PATMuonUserDataEmbedder',
  userFloats = cms.PSet(),
  userInts = cms.PSet(),
  userIntFromBools = cms.PSet(),
  userCands = cms.PSet()
)

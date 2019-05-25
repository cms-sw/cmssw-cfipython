import FWCore.ParameterSet.Config as cms

tausWithUserData = cms.EDProducer('PATTauUserDataEmbedder',
  userFloats = cms.PSet(),
  userInts = cms.PSet(),
  userIntFromBools = cms.PSet(),
  userCands = cms.PSet()
)

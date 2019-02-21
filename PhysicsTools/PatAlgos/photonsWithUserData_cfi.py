import FWCore.ParameterSet.Config as cms

photonsWithUserData = cms.EDProducer('PATPhotonUserDataEmbedder',
  userFloats = cms.PSet(),
  userInts = cms.PSet(),
  userIntFromBools = cms.PSet(),
  userCands = cms.PSet()
)

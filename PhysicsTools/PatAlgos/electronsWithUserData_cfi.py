import FWCore.ParameterSet.Config as cms

electronsWithUserData = cms.EDProducer('PATElectronUserDataEmbedder',
  userFloats = cms.PSet(),
  userInts = cms.PSet(),
  userIntFromBools = cms.PSet(),
  userCands = cms.PSet()
)

import FWCore.ParameterSet.Config as cms

photonsWithUserData = cms.EDProducer('PATPhotonUserDataEmbedder',
  src = cms.required.InputTag,
  parentSrcs = cms.VInputTag(),
  userFloats = cms.PSet(),
  userInts = cms.PSet(),
  userIntFromBools = cms.PSet(),
  userCands = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)

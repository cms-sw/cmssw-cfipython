import FWCore.ParameterSet.Config as cms

photonsWithUserData = cms.EDProducer('PATPhotonUserDataEmbedder',
  src = cms.required.InputTag,
  parentSrcs = cms.VInputTag(),
  userFloats = cms.PSet(
    allowAnyLabel_ = cms.optional.InputTag
  ),
  userInts = cms.PSet(
    allowAnyLabel_ = cms.optional.InputTag
  ),
  userIntFromBools = cms.PSet(
    allowAnyLabel_ = cms.optional.InputTag
  ),
  userCands = cms.PSet(
    allowAnyLabel_ = cms.optional.InputTag
  ),
  mightGet = cms.optional.untracked.vstring
)

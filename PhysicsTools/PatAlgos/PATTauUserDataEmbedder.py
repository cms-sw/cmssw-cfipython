import FWCore.ParameterSet.Config as cms

def PATTauUserDataEmbedder(*args, **kwargs):
  mod = cms.EDProducer('PATTauUserDataEmbedder',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

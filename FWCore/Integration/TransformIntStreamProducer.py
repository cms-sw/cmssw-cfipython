import FWCore.ParameterSet.Config as cms

def TransformIntStreamProducer(**kwargs):
  mod = cms.EDProducer('TransformIntStreamProducer',
    get = cms.required.InputTag,
    offset = cms.uint32(0),
    transformOffset = cms.uint32(1),
    checkTransformNotCalled = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def TransformAsyncIntStreamProducer(*args, **kwargs):
  mod = cms.EDProducer('TransformAsyncIntStreamProducer',
    get = cms.required.InputTag,
    offset = cms.uint32(0),
    transformOffset = cms.uint32(1),
    checkTransformNotCalled = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

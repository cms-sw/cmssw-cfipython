import FWCore.ParameterSet.Config as cms

def TransformAsyncIntProducer(*args, **kwargs):
  mod = cms.EDProducer('TransformAsyncIntProducer',
    get = cms.required.InputTag,
    offset = cms.uint32(0),
    transformOffset = cms.uint32(1),
    checkTransformNotCalled = cms.untracked.bool(False),
    noPut = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

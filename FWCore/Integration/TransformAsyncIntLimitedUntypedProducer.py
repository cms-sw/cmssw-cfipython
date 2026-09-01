import FWCore.ParameterSet.Config as cms

def TransformAsyncIntLimitedUntypedProducer(*args, **kwargs):
  mod = cms.EDProducer('TransformAsyncIntLimitedUntypedProducer',
    get = cms.required.InputTag,
    offset = cms.uint32(0),
    transformOffset = cms.uint32(1),
    checkTransformNotCalled = cms.untracked.bool(False),
    concurrencyLimit = cms.untracked.uint32(1),
    noPut = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

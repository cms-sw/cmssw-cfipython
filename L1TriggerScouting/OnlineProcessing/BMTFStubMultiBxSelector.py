import FWCore.ParameterSet.Config as cms

def BMTFStubMultiBxSelector(*args, **kwargs):
  mod = cms.EDProducer('BMTFStubMultiBxSelector',
    stubsTag = cms.required.InputTag,
    bxWindowLength = cms.required.uint32,
    minNBMTFStub = cms.required.uint32,
    condition = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

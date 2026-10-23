import FWCore.ParameterSet.Config as cms

def TestAlpakaVerifyObjectOnDevice_alpaka(*args, **kwargs):
  mod = cms.EDProducer('TestAlpakaVerifyObjectOnDevice@alpaka',
    source = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def DummyFillDQMStore(*args, **kwargs):
  mod = cms.EDProducer('DummyFillDQMStore',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

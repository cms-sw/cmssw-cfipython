import FWCore.ParameterSet.Config as cms

def DummyFillDQMStore(**kwargs):
  mod = cms.EDProducer('DummyFillDQMStore',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

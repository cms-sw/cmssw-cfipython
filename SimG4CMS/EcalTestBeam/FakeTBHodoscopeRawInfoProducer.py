import FWCore.ParameterSet.Config as cms

def FakeTBHodoscopeRawInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('FakeTBHodoscopeRawInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

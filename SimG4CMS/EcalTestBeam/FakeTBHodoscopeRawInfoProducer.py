import FWCore.ParameterSet.Config as cms

def FakeTBHodoscopeRawInfoProducer(**kwargs):
  mod = cms.EDProducer('FakeTBHodoscopeRawInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def FakeGctInputProducer(**kwargs):
  mod = cms.EDProducer('FakeGctInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

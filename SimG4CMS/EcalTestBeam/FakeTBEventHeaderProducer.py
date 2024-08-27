import FWCore.ParameterSet.Config as cms

def FakeTBEventHeaderProducer(**kwargs):
  mod = cms.EDProducer('FakeTBEventHeaderProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

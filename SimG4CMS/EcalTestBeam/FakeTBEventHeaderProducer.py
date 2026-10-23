import FWCore.ParameterSet.Config as cms

def FakeTBEventHeaderProducer(*args, **kwargs):
  mod = cms.EDProducer('FakeTBEventHeaderProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def LEDTask(*args, **kwargs):
  mod = cms.EDProducer('LEDTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def HFRaddamTask(*args, **kwargs):
  mod = cms.EDProducer('HFRaddamTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

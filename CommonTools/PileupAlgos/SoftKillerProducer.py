import FWCore.ParameterSet.Config as cms

def SoftKillerProducer(*args, **kwargs):
  mod = cms.EDProducer('SoftKillerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

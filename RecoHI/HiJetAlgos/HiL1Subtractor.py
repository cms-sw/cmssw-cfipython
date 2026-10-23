import FWCore.ParameterSet.Config as cms

def HiL1Subtractor(*args, **kwargs):
  mod = cms.EDProducer('HiL1Subtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

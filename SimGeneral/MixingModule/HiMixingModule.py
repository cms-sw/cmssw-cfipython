import FWCore.ParameterSet.Config as cms

def HiMixingModule(*args, **kwargs):
  mod = cms.EDProducer('HiMixingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

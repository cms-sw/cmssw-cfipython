import FWCore.ParameterSet.Config as cms

def PreMixingModule(*args, **kwargs):
  mod = cms.EDProducer('PreMixingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def DataMixingModule(*args, **kwargs):
  mod = cms.EDProducer('DataMixingModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ConditionDumperInEdm(*args, **kwargs):
  mod = cms.EDProducer('ConditionDumperInEdm',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

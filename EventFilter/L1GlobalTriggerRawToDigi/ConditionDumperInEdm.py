import FWCore.ParameterSet.Config as cms

def ConditionDumperInEdm(**kwargs):
  mod = cms.EDProducer('ConditionDumperInEdm',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

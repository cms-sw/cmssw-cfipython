import FWCore.ParameterSet.Config as cms

def ConvertObjectMapRecord(**kwargs):
  mod = cms.EDProducer('ConvertObjectMapRecord',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

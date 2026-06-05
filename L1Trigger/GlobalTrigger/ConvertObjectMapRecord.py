import FWCore.ParameterSet.Config as cms

def ConvertObjectMapRecord(*args, **kwargs):
  mod = cms.EDProducer('ConvertObjectMapRecord',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

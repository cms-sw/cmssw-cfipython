import FWCore.ParameterSet.Config as cms

def CastorTTRecord(**kwargs):
  mod = cms.EDProducer('CastorTTRecord',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def CastorTTRecord(*args, **kwargs):
  mod = cms.EDProducer('CastorTTRecord',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

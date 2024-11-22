import FWCore.ParameterSet.Config as cms

def GeometryProducer(*args, **kwargs):
  mod = cms.EDProducer('GeometryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

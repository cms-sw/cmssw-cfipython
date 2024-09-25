import FWCore.ParameterSet.Config as cms

def DTRecSegment2DProducer(*args, **kwargs):
  mod = cms.EDProducer('DTRecSegment2DProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

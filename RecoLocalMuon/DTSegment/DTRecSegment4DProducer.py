import FWCore.ParameterSet.Config as cms

def DTRecSegment4DProducer(*args, **kwargs):
  mod = cms.EDProducer('DTRecSegment4DProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

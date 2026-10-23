import FWCore.ParameterSet.Config as cms

def DTRecSegment2DExtendedProducer(*args, **kwargs):
  mod = cms.EDProducer('DTRecSegment2DExtendedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def ME0SegmentProducer(*args, **kwargs):
  mod = cms.EDProducer('ME0SegmentProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

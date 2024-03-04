import FWCore.ParameterSet.Config as cms

def ME0SegmentProducer(**kwargs):
  mod = cms.EDProducer('ME0SegmentProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

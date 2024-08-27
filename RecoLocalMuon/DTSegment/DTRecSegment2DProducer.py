import FWCore.ParameterSet.Config as cms

def DTRecSegment2DProducer(**kwargs):
  mod = cms.EDProducer('DTRecSegment2DProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

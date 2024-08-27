import FWCore.ParameterSet.Config as cms

def DTRecSegment4DProducer(**kwargs):
  mod = cms.EDProducer('DTRecSegment4DProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

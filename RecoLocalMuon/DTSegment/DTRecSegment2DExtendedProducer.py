import FWCore.ParameterSet.Config as cms

def DTRecSegment2DExtendedProducer(**kwargs):
  mod = cms.EDProducer('DTRecSegment2DExtendedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

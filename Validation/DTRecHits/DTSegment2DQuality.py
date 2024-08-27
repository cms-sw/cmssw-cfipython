import FWCore.ParameterSet.Config as cms

def DTSegment2DQuality(**kwargs):
  mod = cms.EDProducer('DTSegment2DQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

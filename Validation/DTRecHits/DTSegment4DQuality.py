import FWCore.ParameterSet.Config as cms

def DTSegment4DQuality(**kwargs):
  mod = cms.EDProducer('DTSegment4DQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

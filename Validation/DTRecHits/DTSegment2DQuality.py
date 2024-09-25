import FWCore.ParameterSet.Config as cms

def DTSegment2DQuality(*args, **kwargs):
  mod = cms.EDProducer('DTSegment2DQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

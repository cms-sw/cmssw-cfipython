import FWCore.ParameterSet.Config as cms

def DTSegment4DQuality(*args, **kwargs):
  mod = cms.EDProducer('DTSegment4DQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

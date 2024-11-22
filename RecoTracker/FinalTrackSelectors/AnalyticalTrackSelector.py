import FWCore.ParameterSet.Config as cms

def AnalyticalTrackSelector(*args, **kwargs):
  mod = cms.EDProducer('AnalyticalTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

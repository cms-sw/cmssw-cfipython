import FWCore.ParameterSet.Config as cms

def ConversionTrackRefFix(*args, **kwargs):
  mod = cms.EDProducer('ConversionTrackRefFix',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

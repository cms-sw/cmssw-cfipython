import FWCore.ParameterSet.Config as cms

def ConversionTrackMerger(*args, **kwargs):
  mod = cms.EDProducer('ConversionTrackMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

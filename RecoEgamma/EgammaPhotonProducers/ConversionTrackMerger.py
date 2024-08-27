import FWCore.ParameterSet.Config as cms

def ConversionTrackMerger(**kwargs):
  mod = cms.EDProducer('ConversionTrackMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

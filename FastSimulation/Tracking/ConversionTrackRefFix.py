import FWCore.ParameterSet.Config as cms

def ConversionTrackRefFix(**kwargs):
  mod = cms.EDProducer('ConversionTrackRefFix',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

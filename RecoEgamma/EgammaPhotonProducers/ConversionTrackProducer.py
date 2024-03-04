import FWCore.ParameterSet.Config as cms

def ConversionTrackProducer(**kwargs):
  mod = cms.EDProducer('ConversionTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

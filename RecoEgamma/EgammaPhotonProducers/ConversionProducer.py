import FWCore.ParameterSet.Config as cms

def ConversionProducer(**kwargs):
  mod = cms.EDProducer('ConversionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

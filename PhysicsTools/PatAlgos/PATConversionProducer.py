import FWCore.ParameterSet.Config as cms

def PATConversionProducer(**kwargs):
  mod = cms.EDProducer('PATConversionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

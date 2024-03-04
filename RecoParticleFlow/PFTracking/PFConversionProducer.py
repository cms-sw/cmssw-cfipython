import FWCore.ParameterSet.Config as cms

def PFConversionProducer(**kwargs):
  mod = cms.EDProducer('PFConversionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

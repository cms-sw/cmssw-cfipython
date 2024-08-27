import FWCore.ParameterSet.Config as cms

def PATMHTProducer(**kwargs):
  mod = cms.EDProducer('PATMHTProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

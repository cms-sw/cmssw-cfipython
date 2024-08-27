import FWCore.ParameterSet.Config as cms

def ME0ReDigiProducer(**kwargs):
  mod = cms.EDProducer('ME0ReDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

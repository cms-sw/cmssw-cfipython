import FWCore.ParameterSet.Config as cms

def ME0PadDigiProducer(**kwargs):
  mod = cms.EDProducer('ME0PadDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
import FWCore.ParameterSet.Config as cms

def ExoticaDQM(**kwargs):
  mod = cms.EDProducer('ExoticaDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

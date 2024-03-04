import FWCore.ParameterSet.Config as cms

def Phase2TrackerDigiProducer(**kwargs):
  mod = cms.EDProducer('Phase2TrackerDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

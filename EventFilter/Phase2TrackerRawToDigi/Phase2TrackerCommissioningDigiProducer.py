import FWCore.ParameterSet.Config as cms

def Phase2TrackerCommissioningDigiProducer(**kwargs):
  mod = cms.EDProducer('Phase2TrackerCommissioningDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

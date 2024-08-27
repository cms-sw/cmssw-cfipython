import FWCore.ParameterSet.Config as cms

def L1TrackerEtMissProducer(**kwargs):
  mod = cms.EDProducer('L1TrackerEtMissProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

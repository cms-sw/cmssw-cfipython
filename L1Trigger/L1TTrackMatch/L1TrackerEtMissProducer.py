import FWCore.ParameterSet.Config as cms

def L1TrackerEtMissProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TrackerEtMissProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

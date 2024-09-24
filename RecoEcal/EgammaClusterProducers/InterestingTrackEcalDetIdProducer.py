import FWCore.ParameterSet.Config as cms

def InterestingTrackEcalDetIdProducer(*args, **kwargs):
  mod = cms.EDProducer('InterestingTrackEcalDetIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

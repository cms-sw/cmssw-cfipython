import FWCore.ParameterSet.Config as cms

def InterestingTrackEcalDetIdProducer(**kwargs):
  mod = cms.EDProducer('InterestingTrackEcalDetIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

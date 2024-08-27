import FWCore.ParameterSet.Config as cms

def TrackingTruthValid(**kwargs):
  mod = cms.EDProducer('TrackingTruthValid',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

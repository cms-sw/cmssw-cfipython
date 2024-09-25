import FWCore.ParameterSet.Config as cms

def TrackMultiplicityCounter(*args, **kwargs):
  mod = cms.EDProducer('TrackMultiplicityCounter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def TrackMultiplicityCounter(**kwargs):
  mod = cms.EDProducer('TrackMultiplicityCounter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def TrackOfDSVThingsProducer(**kwargs):
  mod = cms.EDProducer('TrackOfDSVThingsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

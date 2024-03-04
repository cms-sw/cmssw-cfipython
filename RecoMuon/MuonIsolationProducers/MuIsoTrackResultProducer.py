import FWCore.ParameterSet.Config as cms

def MuIsoTrackResultProducer(**kwargs):
  mod = cms.EDProducer('MuIsoTrackResultProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

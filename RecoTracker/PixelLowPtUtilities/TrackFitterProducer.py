import FWCore.ParameterSet.Config as cms

def TrackFitterProducer(**kwargs):
  mod = cms.EDProducer('TrackFitterProducer',
    TTRHBuilder = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

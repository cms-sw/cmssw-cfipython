import FWCore.ParameterSet.Config as cms

def TrackDeepNNTagInfoProducer(**kwargs):
  mod = cms.EDProducer('TrackDeepNNTagInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

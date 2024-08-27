import FWCore.ParameterSet.Config as cms

def TrackWithVertexSelector(**kwargs):
  mod = cms.EDProducer('TrackWithVertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

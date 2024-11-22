import FWCore.ParameterSet.Config as cms

def TrackWithVertexSelector(*args, **kwargs):
  mod = cms.EDProducer('TrackWithVertexSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

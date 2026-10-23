import FWCore.ParameterSet.Config as cms

def PATTrackAndVertexUnpacker(*args, **kwargs):
  mod = cms.EDProducer('PATTrackAndVertexUnpacker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def PATTrackAndVertexUnpacker(**kwargs):
  mod = cms.EDProducer('PATTrackAndVertexUnpacker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

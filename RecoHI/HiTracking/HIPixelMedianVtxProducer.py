import FWCore.ParameterSet.Config as cms

def HIPixelMedianVtxProducer(*args, **kwargs):
  mod = cms.EDProducer('HIPixelMedianVtxProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

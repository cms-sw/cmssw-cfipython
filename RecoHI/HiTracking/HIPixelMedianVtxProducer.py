import FWCore.ParameterSet.Config as cms

def HIPixelMedianVtxProducer(**kwargs):
  mod = cms.EDProducer('HIPixelMedianVtxProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

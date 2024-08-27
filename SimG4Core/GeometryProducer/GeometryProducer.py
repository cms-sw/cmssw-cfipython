import FWCore.ParameterSet.Config as cms

def GeometryProducer(**kwargs):
  mod = cms.EDProducer('GeometryProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

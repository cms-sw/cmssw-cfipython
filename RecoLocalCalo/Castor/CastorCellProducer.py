import FWCore.ParameterSet.Config as cms

def CastorCellProducer(**kwargs):
  mod = cms.EDProducer('CastorCellProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

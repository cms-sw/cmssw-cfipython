import FWCore.ParameterSet.Config as cms

def CastorCellProducer(*args, **kwargs):
  mod = cms.EDProducer('CastorCellProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

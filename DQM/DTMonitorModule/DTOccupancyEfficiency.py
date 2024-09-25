import FWCore.ParameterSet.Config as cms

def DTOccupancyEfficiency(*args, **kwargs):
  mod = cms.EDProducer('DTOccupancyEfficiency',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

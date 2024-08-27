import FWCore.ParameterSet.Config as cms

def DTOccupancyEfficiency(**kwargs):
  mod = cms.EDProducer('DTOccupancyEfficiency',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

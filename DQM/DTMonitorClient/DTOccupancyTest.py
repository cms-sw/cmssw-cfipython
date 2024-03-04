import FWCore.ParameterSet.Config as cms

def DTOccupancyTest(**kwargs):
  mod = cms.EDProducer('DTOccupancyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

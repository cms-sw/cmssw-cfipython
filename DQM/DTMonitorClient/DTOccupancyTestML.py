import FWCore.ParameterSet.Config as cms

def DTOccupancyTestML(**kwargs):
  mod = cms.EDProducer('DTOccupancyTestML',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def ESOccupancyTask(**kwargs):
  mod = cms.EDProducer('ESOccupancyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

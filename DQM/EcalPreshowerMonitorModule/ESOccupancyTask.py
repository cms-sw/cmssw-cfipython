import FWCore.ParameterSet.Config as cms

def ESOccupancyTask(*args, **kwargs):
  mod = cms.EDProducer('ESOccupancyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

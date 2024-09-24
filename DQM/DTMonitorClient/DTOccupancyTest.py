import FWCore.ParameterSet.Config as cms

def DTOccupancyTest(*args, **kwargs):
  mod = cms.EDProducer('DTOccupancyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

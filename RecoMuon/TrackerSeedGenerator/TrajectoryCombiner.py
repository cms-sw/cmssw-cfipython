import FWCore.ParameterSet.Config as cms

def TrajectoryCombiner(**kwargs):
  mod = cms.EDProducer('TrajectoryCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

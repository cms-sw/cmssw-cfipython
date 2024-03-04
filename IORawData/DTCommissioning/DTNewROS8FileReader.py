import FWCore.ParameterSet.Config as cms

def DTNewROS8FileReader(**kwargs):
  mod = cms.EDProducer('DTNewROS8FileReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

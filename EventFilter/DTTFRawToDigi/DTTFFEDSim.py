import FWCore.ParameterSet.Config as cms

def DTTFFEDSim(**kwargs):
  mod = cms.EDProducer('DTTFFEDSim',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def JetEnergyShift(**kwargs):
  mod = cms.EDProducer('JetEnergyShift',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

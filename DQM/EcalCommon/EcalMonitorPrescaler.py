import FWCore.ParameterSet.Config as cms

def EcalMonitorPrescaler(**kwargs):
  mod = cms.EDFilter('EcalMonitorPrescaler',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def EcalMonitorPrescaler(*args, **kwargs):
  mod = cms.EDFilter('EcalMonitorPrescaler',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

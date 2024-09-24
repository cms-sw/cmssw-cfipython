import FWCore.ParameterSet.Config as cms

def EcalSkim(*args, **kwargs):
  mod = cms.EDFilter('EcalSkim',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

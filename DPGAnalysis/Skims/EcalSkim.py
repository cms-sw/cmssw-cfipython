import FWCore.ParameterSet.Config as cms

def EcalSkim(**kwargs):
  mod = cms.EDFilter('EcalSkim',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

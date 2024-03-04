import FWCore.ParameterSet.Config as cms

def EcalTangentFilter(**kwargs):
  mod = cms.EDFilter('EcalTangentFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

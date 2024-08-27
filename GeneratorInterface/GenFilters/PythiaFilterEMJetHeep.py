import FWCore.ParameterSet.Config as cms

def PythiaFilterEMJetHeep(**kwargs):
  mod = cms.EDFilter('PythiaFilterEMJetHeep',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

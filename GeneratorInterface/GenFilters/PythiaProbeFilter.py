import FWCore.ParameterSet.Config as cms

def PythiaProbeFilter(**kwargs):
  mod = cms.EDFilter('PythiaProbeFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

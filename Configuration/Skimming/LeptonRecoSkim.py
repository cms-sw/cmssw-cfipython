import FWCore.ParameterSet.Config as cms

def LeptonRecoSkim(**kwargs):
  mod = cms.EDFilter('LeptonRecoSkim',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

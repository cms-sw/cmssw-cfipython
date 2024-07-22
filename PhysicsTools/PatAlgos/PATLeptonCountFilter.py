import FWCore.ParameterSet.Config as cms

def PATLeptonCountFilter(**kwargs):
  mod = cms.EDFilter('PATLeptonCountFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
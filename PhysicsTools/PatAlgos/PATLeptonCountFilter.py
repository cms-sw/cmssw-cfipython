import FWCore.ParameterSet.Config as cms

def PATLeptonCountFilter(*args, **kwargs):
  mod = cms.EDFilter('PATLeptonCountFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

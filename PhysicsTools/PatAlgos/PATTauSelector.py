import FWCore.ParameterSet.Config as cms

def PATTauSelector(*args, **kwargs):
  mod = cms.EDFilter('PATTauSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
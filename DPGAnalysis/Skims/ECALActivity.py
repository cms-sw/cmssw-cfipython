import FWCore.ParameterSet.Config as cms

def ECALActivity(*args, **kwargs):
  mod = cms.EDFilter('ECALActivity',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def JetIDSelectionFunctorFilter(*args, **kwargs):
  mod = cms.EDFilter('JetIDSelectionFunctorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

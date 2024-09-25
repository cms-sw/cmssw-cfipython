import FWCore.ParameterSet.Config as cms

def PFJetIDSelectionFunctorFilter(*args, **kwargs):
  mod = cms.EDFilter('PFJetIDSelectionFunctorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

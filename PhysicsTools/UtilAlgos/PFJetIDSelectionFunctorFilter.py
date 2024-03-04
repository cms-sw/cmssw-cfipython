import FWCore.ParameterSet.Config as cms

def PFJetIDSelectionFunctorFilter(**kwargs):
  mod = cms.EDFilter('PFJetIDSelectionFunctorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

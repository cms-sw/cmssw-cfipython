import FWCore.ParameterSet.Config as cms

def JetIDSelectionFunctorFilter(**kwargs):
  mod = cms.EDFilter('JetIDSelectionFunctorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

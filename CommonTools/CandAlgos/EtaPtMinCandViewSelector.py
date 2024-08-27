import FWCore.ParameterSet.Config as cms

def EtaPtMinCandViewSelector(**kwargs):
  mod = cms.EDFilter('EtaPtMinCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

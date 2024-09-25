import FWCore.ParameterSet.Config as cms

def RetrievePPSAssociationCuts(*args, **kwargs):
  mod = cms.EDAnalyzer('RetrievePPSAssociationCuts',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

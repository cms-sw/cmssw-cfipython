import FWCore.ParameterSet.Config as cms

def L1MenuViewer(**kwargs):
  mod = cms.EDAnalyzer('L1MenuViewer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

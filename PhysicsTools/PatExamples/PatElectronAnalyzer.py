import FWCore.ParameterSet.Config as cms

def PatElectronAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatElectronAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

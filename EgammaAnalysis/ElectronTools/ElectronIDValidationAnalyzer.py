import FWCore.ParameterSet.Config as cms

def ElectronIDValidationAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ElectronIDValidationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

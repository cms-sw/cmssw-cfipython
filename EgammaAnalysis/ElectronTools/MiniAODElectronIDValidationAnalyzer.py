import FWCore.ParameterSet.Config as cms

def MiniAODElectronIDValidationAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('MiniAODElectronIDValidationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

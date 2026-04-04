import FWCore.ParameterSet.Config as cms

def MiniAODElectronIDValidationAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MiniAODElectronIDValidationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

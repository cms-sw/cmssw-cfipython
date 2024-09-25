import FWCore.ParameterSet.Config as cms

def EcalMappingElectronicsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalMappingElectronicsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

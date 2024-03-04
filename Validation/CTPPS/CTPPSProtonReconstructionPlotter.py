import FWCore.ParameterSet.Config as cms

def CTPPSProtonReconstructionPlotter(**kwargs):
  mod = cms.EDAnalyzer('CTPPSProtonReconstructionPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

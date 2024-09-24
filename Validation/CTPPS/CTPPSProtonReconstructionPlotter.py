import FWCore.ParameterSet.Config as cms

def CTPPSProtonReconstructionPlotter(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSProtonReconstructionPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

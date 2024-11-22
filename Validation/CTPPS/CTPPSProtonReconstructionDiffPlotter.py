import FWCore.ParameterSet.Config as cms

def CTPPSProtonReconstructionDiffPlotter(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSProtonReconstructionDiffPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

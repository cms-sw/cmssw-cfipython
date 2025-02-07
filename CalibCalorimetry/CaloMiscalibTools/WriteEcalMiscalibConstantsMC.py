import FWCore.ParameterSet.Config as cms

def WriteEcalMiscalibConstantsMC(*args, **kwargs):
  mod = cms.EDAnalyzer('WriteEcalMiscalibConstantsMC',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

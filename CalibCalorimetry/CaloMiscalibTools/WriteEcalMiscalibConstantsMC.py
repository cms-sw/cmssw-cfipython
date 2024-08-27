import FWCore.ParameterSet.Config as cms

def WriteEcalMiscalibConstantsMC(**kwargs):
  mod = cms.EDAnalyzer('WriteEcalMiscalibConstantsMC',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

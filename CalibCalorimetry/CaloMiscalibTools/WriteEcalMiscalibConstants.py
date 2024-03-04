import FWCore.ParameterSet.Config as cms

def WriteEcalMiscalibConstants(**kwargs):
  mod = cms.EDAnalyzer('WriteEcalMiscalibConstants',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

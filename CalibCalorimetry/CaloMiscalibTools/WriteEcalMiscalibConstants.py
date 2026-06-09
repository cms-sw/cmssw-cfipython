import FWCore.ParameterSet.Config as cms

def WriteEcalMiscalibConstants(*args, **kwargs):
  mod = cms.EDAnalyzer('WriteEcalMiscalibConstants',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

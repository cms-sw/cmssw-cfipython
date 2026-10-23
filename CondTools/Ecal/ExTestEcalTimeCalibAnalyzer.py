import FWCore.ParameterSet.Config as cms

def ExTestEcalTimeCalibAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTimeCalibAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

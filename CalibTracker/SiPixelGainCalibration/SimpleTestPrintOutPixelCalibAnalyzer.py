import FWCore.ParameterSet.Config as cms

def SimpleTestPrintOutPixelCalibAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SimpleTestPrintOutPixelCalibAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

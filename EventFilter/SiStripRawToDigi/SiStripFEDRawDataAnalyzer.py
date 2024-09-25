import FWCore.ParameterSet.Config as cms

def SiStripFEDRawDataAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripFEDRawDataAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def SiStripFEDRawDataAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SiStripFEDRawDataAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

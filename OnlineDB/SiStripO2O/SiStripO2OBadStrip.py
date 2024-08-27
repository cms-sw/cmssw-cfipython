import FWCore.ParameterSet.Config as cms

def SiStripO2OBadStrip(**kwargs):
  mod = cms.EDAnalyzer('SiStripO2OBadStrip',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

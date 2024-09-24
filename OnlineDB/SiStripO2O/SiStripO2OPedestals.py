import FWCore.ParameterSet.Config as cms

def SiStripO2OPedestals(**kwargs):
  mod = cms.EDAnalyzer('SiStripO2OPedestals',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
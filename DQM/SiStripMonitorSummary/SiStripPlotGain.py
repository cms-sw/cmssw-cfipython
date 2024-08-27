import FWCore.ParameterSet.Config as cms

def SiStripPlotGain(**kwargs):
  mod = cms.EDAnalyzer('SiStripPlotGain',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

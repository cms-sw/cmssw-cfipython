import FWCore.ParameterSet.Config as cms

def SiStripPlotGain(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPlotGain',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def HcalQLPlotAnal(**kwargs):
  mod = cms.EDAnalyzer('HcalQLPlotAnal',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

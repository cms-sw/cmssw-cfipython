import FWCore.ParameterSet.Config as cms

def L1GtRunSettingsViewer(**kwargs):
  mod = cms.EDAnalyzer('L1GtRunSettingsViewer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

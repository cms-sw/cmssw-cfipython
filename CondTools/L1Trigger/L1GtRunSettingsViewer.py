import FWCore.ParameterSet.Config as cms

def L1GtRunSettingsViewer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1GtRunSettingsViewer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

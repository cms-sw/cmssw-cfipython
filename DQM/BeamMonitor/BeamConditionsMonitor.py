import FWCore.ParameterSet.Config as cms

def BeamConditionsMonitor(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamConditionsMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

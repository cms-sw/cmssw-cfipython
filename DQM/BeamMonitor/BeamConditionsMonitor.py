import FWCore.ParameterSet.Config as cms

def BeamConditionsMonitor(**kwargs):
  mod = cms.EDAnalyzer('BeamConditionsMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

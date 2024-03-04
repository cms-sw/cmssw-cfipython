import FWCore.ParameterSet.Config as cms

def BeamMonitorBx(**kwargs):
  mod = cms.EDAnalyzer('BeamMonitorBx',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

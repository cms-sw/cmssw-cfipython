import FWCore.ParameterSet.Config as cms

def AlcaBeamMonitorClient(*args, **kwargs):
  mod = cms.EDAnalyzer('AlcaBeamMonitorClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def AlcaBeamMonitorClient(**kwargs):
  mod = cms.EDAnalyzer('AlcaBeamMonitorClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def AlcaBeamSpotHarvester(*args, **kwargs):
  mod = cms.EDAnalyzer('AlcaBeamSpotHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

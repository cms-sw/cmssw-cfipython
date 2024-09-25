import FWCore.ParameterSet.Config as cms

def BeamSpotFakeConditions(*args, **kwargs):
  mod = cms.ESSource('BeamSpotFakeConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

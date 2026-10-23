import FWCore.ParameterSet.Config as cms

def CSCFakeDBNoiseMatrix(*args, **kwargs):
  mod = cms.ESSource('CSCFakeDBNoiseMatrix',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

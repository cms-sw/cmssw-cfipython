import FWCore.ParameterSet.Config as cms

def CSCFakeDBNoiseMatrix(**kwargs):
  mod = cms.ESSource('CSCFakeDBNoiseMatrix',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def FakeAlignmentSource(**kwargs):
  mod = cms.ESSource('FakeAlignmentSource',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

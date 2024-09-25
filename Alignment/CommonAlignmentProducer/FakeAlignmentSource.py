import FWCore.ParameterSet.Config as cms

def FakeAlignmentSource(*args, **kwargs):
  mod = cms.ESSource('FakeAlignmentSource',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

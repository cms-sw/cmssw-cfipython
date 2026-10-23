import FWCore.ParameterSet.Config as cms

def AlignmentProducer(*args, **kwargs):
  mod = cms.Looper('AlignmentProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

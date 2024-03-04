import FWCore.ParameterSet.Config as cms

def AlignmentProducer(**kwargs):
  mod = cms.EDLooper('AlignmentProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

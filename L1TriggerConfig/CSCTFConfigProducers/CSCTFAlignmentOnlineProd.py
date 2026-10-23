import FWCore.ParameterSet.Config as cms

def CSCTFAlignmentOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('CSCTFAlignmentOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

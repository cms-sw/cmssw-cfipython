import FWCore.ParameterSet.Config as cms

def MkFitIterationConfigESProducer(**kwargs):
  mod = cms.ESProducer('MkFitIterationConfigESProducer',
    ComponentName = cms.string(''),
    config = cms.FileInPath(''),
    minPt = cms.double(0),
    maxClusterSize = cms.uint32(8),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

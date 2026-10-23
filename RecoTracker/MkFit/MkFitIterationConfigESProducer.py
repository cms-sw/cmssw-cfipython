import FWCore.ParameterSet.Config as cms

def MkFitIterationConfigESProducer(*args, **kwargs):
  mod = cms.ESProducer('MkFitIterationConfigESProducer',
    ComponentName = cms.string(''),
    config = cms.FileInPath(''),
    minPt = cms.double(0),
    maxClusterSize = cms.uint32(8),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

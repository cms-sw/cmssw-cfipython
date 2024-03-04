import FWCore.ParameterSet.Config as cms

def RawStreamFileWriterForBU(**kwargs):
  mod = cms.OutputModule('RawStreamFileWriterForBU',
    source = cms.InputTag('rawDataCollector'),
    numEventsPerFile = cms.uint32(100),
    frdVersion = cms.uint32(6),
    microSleep = cms.int32(0),
    frdFileVersion = cms.uint32(0)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

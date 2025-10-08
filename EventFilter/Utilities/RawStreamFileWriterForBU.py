import FWCore.ParameterSet.Config as cms

def RawStreamFileWriterForBU(*args, **kwargs):
  mod = cms.OutputModule('RawStreamFileWriterForBU',
    source = cms.InputTag('rawDataCollector'),
    numEventsPerFile = cms.uint32(100),
    frdVersion = cms.uint32(6),
    rawProductName = cms.untracked.string('FEDRawDataCollection'),
    sourceIdList = cms.untracked.vuint32(),
    writeToOpen = cms.untracked.bool(False),
    microSleep = cms.int32(0),
    frdFileVersion = cms.uint32(0),
    dataType = cms.untracked.uint32(0),
    writeEoR = cms.untracked.bool(True)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

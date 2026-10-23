import FWCore.ParameterSet.Config as cms

def GEMRawToDigiModule(*args, **kwargs):
  mod = cms.EDProducer('GEMRawToDigiModule',
    InputLabel = cms.InputTag('rawDataCollector'),
    useDBEMap = cms.bool(False),
    keepDAQStatus = cms.bool(True),
    readMultiBX = cms.bool(False),
    ge21Off = cms.bool(False),
    fedIdStart = cms.uint32(1467),
    fedIdEnd = cms.uint32(1478),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

muonGEMDigisDefault = cms.EDProducer('GEMRawToDigiModule',
  InputLabel = cms.InputTag('rawDataCollector'),
  useDBEMap = cms.bool(False),
  keepDAQStatus = cms.bool(True),
  readMultiBX = cms.bool(False),
  ge21Off = cms.bool(False),
  fedIdStart = cms.uint32(1467),
  fedIdEnd = cms.uint32(1478),
  mightGet = cms.optional.untracked.vstring
)

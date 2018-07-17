import FWCore.ParameterSet.Config as cms

fastTimerServiceClient = cms.EDProducer('FastTimerServiceClient',
  dqmPath = cms.untracked.string('HLT/TimerService'),
  doPlotsVsScalLumi = cms.bool(True),
  doPlotsVsPixelLumi = cms.bool(False),
  doPlotsVsPU = cms.bool(True),
  scalLumiME = cms.PSet(
    folder = cms.string('HLT/LumiMonitoring'),
    name = cms.string('lumiVsLS'),
    nbins = cms.int32(440),
    xmin = cms.double(0),
    xmax = cms.double(22000)
  ),
  pixelLumiME = cms.PSet(
    folder = cms.string('HLT/LumiMonitoring'),
    name = cms.string('lumiVsLS'),
    nbins = cms.int32(440),
    xmin = cms.double(0),
    xmax = cms.double(22000)
  ),
  puME = cms.PSet(
    folder = cms.string('HLT/LumiMonitoring'),
    name = cms.string('puVsLS'),
    nbins = cms.int32(260),
    xmin = cms.double(0),
    xmax = cms.double(130)
  )
)

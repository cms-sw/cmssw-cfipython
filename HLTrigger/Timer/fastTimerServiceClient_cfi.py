import FWCore.ParameterSet.Config as cms

fastTimerServiceClient = cms.EDAnalyzer('FastTimerServiceClient',
  dqmPath = cms.untracked.string('HLT/TimerService'),
  doPlotsVsScalLumi = cms.bool(True),
  doPlotsVsPixelLumi = cms.bool(False),
  scalLumiME = cms.PSet(
    folder = cms.string('HLT/LumiMonitoring'),
    name = cms.string('lumiVsLS'),
    nbins = cms.int32(6500),
    xmin = cms.double(0),
    xmax = cms.double(13000)
  ),
  pixelLumiME = cms.PSet(
    folder = cms.string('HLT/LumiMonitoring'),
    name = cms.string('lumiVsLS'),
    nbins = cms.int32(6500),
    xmin = cms.double(0),
    xmax = cms.double(13000)
  )
)

import FWCore.ParameterSet.Config as cms

ctppsLHCInfoPlotterDefault = cms.EDAnalyzer('CTPPSLHCInfoPlotter',
  lhcInfoLabel = cms.string(''),
  lhcInfoPerLSLabel = cms.string(''),
  lhcInfoPerFillLabel = cms.string(''),
  useNewLHCInfo = cms.bool(False),
  outputFile = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

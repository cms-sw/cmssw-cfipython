import FWCore.ParameterSet.Config as cms

ctppsHepMCDistributionPlotterDefault = cms.EDAnalyzer('CTPPSHepMCDistributionPlotter',
  lhcInfoLabel = cms.string(''),
  lhcInfoPerLSLabel = cms.string(''),
  lhcInfoPerFillLabel = cms.string(''),
  useNewLHCInfo = cms.bool(False),
  outputFile = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)

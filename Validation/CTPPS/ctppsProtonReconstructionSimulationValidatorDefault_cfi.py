import FWCore.ParameterSet.Config as cms

ctppsProtonReconstructionSimulationValidatorDefault = cms.EDAnalyzer('CTPPSProtonReconstructionSimulationValidator',
  lhcInfoLabel = cms.string(''),
  lhcInfoPerLSLabel = cms.string(''),
  lhcInfoPerFillLabel = cms.string(''),
  useNewLHCInfo = cms.bool(False),
  outputFile = cms.string('output.root'),
  verbosity = cms.untracked.uint32(0),
  mightGet = cms.optional.untracked.vstring
)

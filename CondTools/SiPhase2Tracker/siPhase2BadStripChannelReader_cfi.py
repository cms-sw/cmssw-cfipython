import FWCore.ParameterSet.Config as cms

siPhase2BadStripChannelReader = cms.EDAnalyzer('SiPhase2BadStripChannelReader',
  printVerbose = cms.untracked.bool(False),
  printDebug = cms.untracked.int32(1),
  label = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)

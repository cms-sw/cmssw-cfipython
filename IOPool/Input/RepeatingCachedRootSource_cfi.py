import FWCore.ParameterSet.Config as cms

source = cms.Source('RepeatingCachedRootSource',
  fileName = cms.required.untracked.string,
  repeatNEvents = cms.untracked.uint32(10),
  skipEvents = cms.untracked.uint32(0),
  inputCommands = cms.untracked.vstring('keep *'),
  processingMode = cms.untracked.string('RunsLumisAndEvents'),
  writeStatusFile = cms.untracked.bool(False)
)
